from database.conexion import get_db_connection
from utilidades.excepciones import DatabaseError, NotFoundError
import sqlite3

class PacienteModel:
    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pacientes")
            # Convierte las filas obtenidas en diccionarios para facilitar su manejo y serialización
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(id_paciente: int):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            row = cursor.fetchone()
            if not row:
                raise NotFoundError(f"Paciente con ID {id_paciente} no encontrado.")
            return dict(row)

    @staticmethod
    def get_by_dni(dni: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pacientes WHERE dni = ?", (dni,))
            row = cursor.fetchone()
            # Devuelve None si no existe para que la capa superior valide si el DNI está duplicado
            return dict(row) if row else None

    @staticmethod
    def create(nombre: str, dni: str, telefono: str, fecha_nacimiento: str):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO pacientes (nombre, dni, telefono, fecha_nacimiento) VALUES (?, ?, ?, ?)",
                    (nombre, dni, telefono, fecha_nacimiento)
                )
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            # Captura la violación de la restricción UNIQUE del DNI en la base de datos
            raise DatabaseError(f"Ya existe un paciente con el DNI {dni}.")
        except sqlite3.Error as e:
            raise DatabaseError(f"Error al crear paciente: {e}")

    @staticmethod
    def update(id_paciente: int, nombre: str, telefono: str, fecha_nacimiento: str):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE pacientes SET nombre = ?, telefono = ?, fecha_nacimiento = ? WHERE id_paciente = ?",
                    (nombre, telefono, fecha_nacimiento, id_paciente)
                )
                # rowcount verifica si la query realmente modificó alguna fila en la base de datos
                if cursor.rowcount == 0:
                    raise NotFoundError(f"Paciente con ID {id_paciente} no encontrado.")
        except sqlite3.Error as e:
            raise DatabaseError(f"Error al actualizar paciente: {e}")

    @staticmethod
    def delete(id_paciente: int):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente,))
            # Si rowcount es 0 significa que el ID solicitado no existía antes de borrar
            if cursor.rowcount == 0:
                raise NotFoundError(f"Paciente con ID {id_paciente} no encontrado.")