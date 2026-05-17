from servicios.medico_service import MedicoService
from utilidades.ayudas import clear_screen, print_header, print_table, input_int
from utilidades.excepciones import HospitalManagerError

def menu_medicos():
    while True:
        clear_screen()
        print_header("GESTIÓN DE MÉDICOS")
        print("1. Listar Médicos")
        print("2. Registrar Nuevo Médico")
        print("3. Actualizar Médico")
        print("4. Eliminar Médico")
        print("0. Volver al Menú Principal\n")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            _listar_medicos()
        elif opcion == '2':
            _crear_medico()
        elif opcion == '3':
            _actualizar_medico()
        elif opcion == '4':
            _eliminar_medico()
        elif opcion == '0':
            break