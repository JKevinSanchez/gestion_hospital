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

def _listar_medicos():
    clear_screen()
    print_header("LISTADO DE MÉDICOS")
    medicos = MedicoService.listar_medicos()
    if medicos:
        headers = ["ID", "Nombre", "Especialidad"]
        rows = [[m['id_medico'], m['nombre'], m['especialidad']] for m in medicos]
        print_table(headers, rows)
    else:
        print("No hay médicos registrados.")
    input("Presiona Enter para continuar...")

def _crear_medico():
    clear_screen()
    print_header("NUEVO MÉDICO")
    nombre = input("Nombre del médico: ")
    especialidad = input("Especialidad: ")
    
    try:
        MedicoService.crear_medico(nombre, especialidad)
        print("\n✅ Médico creado correctamente.")
    except HospitalManagerError as e:
        print(f"\n❌ Error: {e}")
    input("\nPresiona Enter para continuar...")

def _actualizar_medico():
    clear_screen()
    print_header("ACTUALIZAR MÉDICO")
    id_medico = input_int("ID del médico a actualizar (0 para cancelar)")
    if id_medico == 0: return
    
    nombre = input("Nuevo nombre: ")
    especialidad = input("Nueva especialidad: ")
    
    try:
        MedicoService.actualizar_medico(id_medico, nombre, especialidad)
        print("\n✅ Médico actualizado correctamente.")
    except HospitalManagerError as e:
        print(f"\n❌ Error: {e}")
    input("\nPresiona Enter para continuar...")

def _eliminar_medico():
    clear_screen()
    print_header("ELIMINAR MÉDICO")
    id_medico = input_int("ID del médico a eliminar (0 para cancelar)")
    if id_medico == 0: return
    
    try:
        MedicoService.eliminar_medico(id_medico)
        print("\n✅ Médico eliminado correctamente.")
    except HospitalManagerError as e:
        print(f"\n❌ Error: {e}")
    input("\nPresiona Enter para continuar...")
