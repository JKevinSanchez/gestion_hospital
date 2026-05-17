import sqlite3
from contextlib import contextmanager
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'hospital.db')

@contextmanager
def get_db_connection():
    """
    Context manager para manejar la conexión a la base de datos.
    Asegura que la conexión se cierra, ejecuta commit en éxito y rollback en error.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        # Habilitar claves foráneas en SQLite (es necesario activarlo por conexión)
        conn.execute("PRAGMA foreign_keys = ON;")
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def init_db():
    """Inicializa la base de datos creando las tablas según el esquema."""
    esquema_path = os.path.join(os.path.dirname(__file__), 'esquema.sql')
    if not os.path.exists(esquema_path):
        return

    with sqlite3.connect(DB_PATH) as conn:
        with open(esquema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()

def seed_db():
    """Puebla la base de datos con datos iniciales si está vacía."""
    semilla_path = os.path.join(os.path.dirname(__file__), 'semilla.sql')
    if not os.path.exists(semilla_path):
        return

    with sqlite3.connect(DB_PATH) as conn:
        # Comprobar si ya hay pacientes para no duplicar en cada ejecución
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes")
        if cursor.fetchone()[0] == 0:
            with open(semilla_path, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
            conn.commit()
