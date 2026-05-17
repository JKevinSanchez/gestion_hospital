from utilidades.ayudas import clear_screen, print_header
from menus.paciente_menu import menu_pacientes
from menus.medico_menu import menu_medicos
from menus.cita_menu import menu_citas

def main_menu():
    """Bucle principal de la aplicación."""
    # Mantiene la aplicación activa hasta que el usuario decida salir explícitamente (opción 0)
    while True:
        clear_screen()
        print_header("HOSPITAL MANAGER")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Citas")
        print("0. Salir\n")
        
        opcion = input("Selecciona una opción: ").strip()
        
        # Enrutamiento hacia los submódulos de gestión correspondientes
        if opcion == '1':
            menu_pacientes()
        elif opcion == '2':
            menu_medicos()
        elif opcion == '3':
            menu_citas()
        elif opcion == '0':
            clear_screen()
            print("¡Gracias por usar Hospital Manager! Hasta pronto.\n")
            break  # Rompe el bucle para finalizar la ejecución del programa
        else:
            print("Opción no válida.")
            # Pausa el flujo para que el usuario pueda leer el mensaje de error antes de limpiar la pantalla
            input("Presiona Enter para continuar...")