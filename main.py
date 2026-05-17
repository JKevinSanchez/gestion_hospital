import sys
import os

# Asegurar que el directorio raíz está en el path para las importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.conexion import init_db, seed_db
from menus.main_menu import main_menu

def main():
    try:
        # Inicializa las tablas y carga los datos de prueba iniciales
        init_db()
        seed_db()
        
        # Lanza el bucle de la interfaz de usuario en consola
        main_menu()
    except KeyboardInterrupt:
        # Captura la interrupción manual del usuario (ej. Ctrl+C) para un cierre limpio
        print("\n\nCierre forzado. ¡Hasta pronto!")
    except Exception as e:
        # Captura cualquier fallo crítico no controlado en la aplicación
        print(f"\n[ERROR FATAL] {e}")

if __name__ == "__main__":
    main()