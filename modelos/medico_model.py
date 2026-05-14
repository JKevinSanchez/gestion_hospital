from database.conexion import get_db_conexion
from utilidades.excepciones import DatabaseError, NotFoundError
import sqlite3

class MedicoModelo:
    @staticmethod
    def obtener_todos():
        with get_db_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medicos")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def obtener_por_id(id_medico: int):
        with get_db_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medicos WHERE id_medico = ?", (id_medico,))
            row = cursor.fetchone()
            if not row:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")
            return dict(row)

    @staticmethod
    def crear(nombre: str, especialidad: str):
        try:
            with get_db_conexion() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO medicos (nombre, especialidad) VALUES (?, ?)",
                    (nombre, especialidad)
                )
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise DatabaseError(f"Error al crear médico: {e}")

    @staticmethod
    def actualizar(id_medico: int, nombre: str, especialidad: str):
        with get_db_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE medicos SET nombre = ?, especialidad = ? WHERE id_medico = ?",
                (nombre, especialidad, id_medico)
            )
            if cursor.rowcount == 0:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")

    @staticmethod
    def eliminar(id_medico: int):
        with get_db_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medicos WHERE id_medico = ?", (id_medico,))
            if cursor.rowcount == 0:
                raise NotFoundError(f"Médico con ID {id_medico} no encontrado.")