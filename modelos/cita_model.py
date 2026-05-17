from database.connection import get_db_connection
from utils.exceptions import DatabaseError, NotFoundError
import sqlite3

class CitaModel:
    @staticmethod
    def get_all_details():
        query = """
            SELECT c.id_cita, p.nombre AS paciente, m.nombre AS medico, c.fecha, c.estado
            FROM citas c
            JOIN pacientes p ON c.id_paciente = p.id_paciente
            JOIN medicos m ON c.id_medico = m.id_medico
            ORDER BY c.fecha
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def check_availability(id_medico: int, fecha: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM citas WHERE id_medico = ? AND fecha = ?",
                (id_medico, fecha)
            )
            count = cursor.fetchone()[0]
            return count == 0

    @staticmethod
    def create_with_transaction(id_paciente: int, id_medico: int, fecha: str):
        # Esta es la implementación de la transacción: verificar disponibilidad e insertar.
        # En caso de error, el get_db_connection context manager hace rollback automáticamente.
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # 1. Verificar si el paciente y médico existen (validación extra para evitar violar FK antes de llegar a la inserción si es posible)
                cursor.execute("SELECT 1 FROM pacientes WHERE id_paciente = ?", (id_paciente,))
                if not cursor.fetchone():
                     raise DatabaseError(f"Paciente con ID {id_paciente} no existe.")
                     
                cursor.execute("SELECT 1 FROM medicos WHERE id_medico = ?", (id_medico,))
                if not cursor.fetchone():
                     raise DatabaseError(f"Médico con ID {id_medico} no existe.")

                # 2. Verificar disponibilidad de nuevo (dentro de la transacción)
                cursor.execute(
                    "SELECT COUNT(*) FROM citas WHERE id_medico = ? AND fecha = ?",
                    (id_medico, fecha)
                )
                if cursor.fetchone()[0] > 0:
                    raise DatabaseError("El médico ya tiene una cita en esa fecha y hora.")
                
                # 3. Insertar
                cursor.execute(
                    "INSERT INTO citas (id_paciente, id_medico, fecha) VALUES (?, ?, ?)",
                    (id_paciente, id_medico, fecha)
                )
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise DatabaseError(f"Error al crear cita: {e}")