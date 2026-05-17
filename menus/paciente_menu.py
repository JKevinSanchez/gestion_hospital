from servicios.paciente_service import PacienteService
from utilidades.ayudas import clear_screen, print_header, print_table, input_int
from utilidades.excepciones import HospitalManagerError

def menu_pacientes():
    """Bucle del menú principal para gestionar pacientes."""
    while True:
        clear_screen()
        print_header("GESTIÓN DE PACIENTES")
        print("1. Listar Pacientes\n2. Registrar Nuevo Paciente\n3. Actualizar Paciente\n4. Eliminar Paciente\n0. Volver al Menú Principal\n")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1': _listar_pacientes()
        elif opcion == '2': _crear_paciente()
        elif opcion == '3': _actualizar_paciente()
        elif opcion == '4': _eliminar_paciente()
        elif opcion == '0': break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

def _listar_pacientes():
    """Muestra la tabla completa de pacientes registrados."""
    clear_screen()
    print_header("LISTADO DE PACIENTES")
    pacientes = PacienteService.listar_pacientes()
    if pacientes:
        headers = ["ID", "Nombre", "DNI", "Teléfono", "Fecha Nac."]
        rows = [[p['id_paciente'], p['nombre'], p['dni'], p['telefono'], p['fecha_nacimiento']] for p in pacientes]
        print_table(headers, rows)
    else:
        print("No hay pacientes registrados.")
    input("Presiona Enter para continuar...")

def _crear_paciente():
    """Registra un nuevo paciente pidiendo datos por consola."""
    clear_screen()
    print_header("NUEVO PACIENTE")
    
    nombre = input("Nombre completo: ")
    dni = input("DNI (ej: 12345678A): ")
    telefono = input("Teléfono: ")
    fecha = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    
    try:
        PacienteService.crear_paciente(nombre, dni, telefono, fecha)
        print("\nPaciente creado correctamente.")
    except HospitalManagerError as e:
        print(f"\n Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def _actualizar_paciente():
    """Modifica datos de un paciente (Enter mantiene el valor actual)."""
    clear_screen()
    print_header("ACTUALIZAR PACIENTE")
    
    _listar_pacientes_sin_pausa()
    id_paciente = input_int("\nID del paciente a actualizar (0 para cancelar)")
    if id_paciente == 0: return

    print("\nDeja el campo vacío si no quieres modificarlo.")
    try:
        paciente = PacienteService.obtener_paciente(id_paciente)
        nombre = input(f"Nombre [{paciente['nombre']}]: ") or paciente['nombre']
        telefono = input(f"Teléfono [{paciente['telefono']}]: ") or paciente['telefono']
        fecha = input(f"Fecha Nacimiento [{paciente['fecha_nacimiento']}]: ") or paciente['fecha_nacimiento']
        
        PacienteService.actualizar_paciente(id_paciente, nombre, telefono, fecha)
        print("\nPaciente actualizado correctamente.")
    except HospitalManagerError as e:
        print(f"\nError: {e}")
    
    input("\nPresiona Enter para continuar...")

def _eliminar_paciente():
    """Elimina un paciente por ID tras confirmación."""
    clear_screen()
    print_header("ELIMINAR PACIENTE")
    
    _listar_pacientes_sin_pausa()
    id_paciente = input_int("\nID del paciente a eliminar (0 para cancelar)")
    if id_paciente == 0: return
    
    confirm = input("¿Estás seguro de eliminar este paciente? (s/N): ")
    if confirm.lower() == 's':
        try:
            PacienteService.eliminar_paciente(id_paciente)
            print("\nPaciente eliminado correctamente.")
        except HospitalManagerError as e:
            print(f"\nError: {e}")
            
    input("\nPresiona Enter para continuar...")

def _listar_pacientes_sin_pausa():
    """Muestra una lista rápida (ID, Nombre, DNI)"""
    pacientes = PacienteService.listar_pacientes()
    if pacientes:
        headers = ["ID", "Nombre", "DNI"]
        rows = [[p['id_paciente'], p['nombre'], p['dni']] for p in pacientes]
        print_table(headers, rows)
