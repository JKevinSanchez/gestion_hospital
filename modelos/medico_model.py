from database.conexion import get_db_connection
from utilidades.excepciones import DatabaseError, NotFoundError
import sqlite3

class MedicoModel:
    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medicos")
            # Convierte las filas obtenidas en una lista de diccionarios
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(id_medico: int):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medicos WHERE id_medico = ?", (id_medico,))
            row = cursor.fetchone()
            # Convierte las filas obtenidas en una lista de diccionarios
            if not row:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")
            return dict(row)

    @staticmethod
    def create(nombre: str, especialidad: str):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO medicos (nombre, especialidad) VALUES (?, ?)",
                    (nombre, especialidad)
                )
                # Retorna el ID del nuevo registro creado
                return cursor.lastrowid
        except sqlite3.Error as e:
            # Captura el error de SQLite y lanza la excepción propia
            raise DatabaseError(f"Error al crear médico: {e}")

    @staticmethod
    def update(id_medico: int, nombre: str, especialidad: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE medicos SET nombre = ?, especialidad = ? WHERE id_medico = ?",
                (nombre, especialidad, id_medico)
            )
            # Si no se modificó ninguna fila, el ID no existía
            if cursor.rowcount == 0:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")

    @staticmethod
    def delete(id_medico: int):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medicos WHERE id_medico = ?", (id_medico,))
            # Si no se eliminó ninguna fila, el ID no existía
            if cursor.rowcount == 0:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")