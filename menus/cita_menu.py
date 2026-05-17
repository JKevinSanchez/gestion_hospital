from servicios.cita_service import CitaService
from servicios.paciente_service import PacienteService
from servicios.medico_service import MedicoService
from utilidades.ayudas import clear_screen, print_header, print_table, input_int
from utilidades.excepciones import HospitalManagerError

def menu_citas():
    while True:
        clear_screen()
        print_header("GESTIÓN DE CITAS")
        print("1. Listar Citas (con detalles)")
        print("2. Agendar Nueva Cita")
        print("3. Cambiar Estado de Cita")
        print("4. Eliminar Cita")
        print("5. Reporte: Médico con más citas")
        print("0. Volver al Menú Principal\n")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            _listar_citas()
        elif opcion == '2':
            _crear_cita()
        elif opcion == '3':
            _cambiar_estado()
        elif opcion == '4':
            _eliminar_cita()
        elif opcion == '5':
            _medico_mas_citas()
        elif opcion == '0':
            break

def _listar_citas():
    clear_screen()
    print_header("LISTADO DE CITAS")
    citas = CitaService.listar_citas()
    if citas:
        headers = ["ID", "Paciente", "Médico", "Fecha", "Estado"]
        rows = [[c['id_cita'], c['paciente'], c['medico'], c['fecha'], c['estado']] for c in citas]
        print_table(headers, rows)
    else:
        print("No hay citas registradas.")
    input("Presiona Enter para continuar...")

def _crear_cita():
    clear_screen()
    print_header("AGENDAR NUEVA CITA")
    
    # Mostrar brevemente pacientes y médicos para ayuda
    print("--- PACIENTES ---")
    for p in PacienteService.listar_pacientes()[:5]:
        print(f"[{p['id_paciente']}] {p['nombre']}")
        
    print("\n--- MÉDICOS ---")
    for m in MedicoService.listar_medicos()[:5]:
        print(f"[{m['id_medico']}] {m['nombre']} ({m['especialidad']})")
    
    print("\n" + "-"*30)
    id_paciente = input_int("ID del paciente")
    id_medico = input_int("ID del médico")
    fecha = input("Fecha y hora de la cita (YYYY-MM-DD HH:MM): ")
    
    try:
        CitaService.crear_cita(id_paciente, id_medico, fecha)
        print("\nCita agendada correctamente.")
    except HospitalManagerError as e:
        print(f"\nError al agendar: {e}")
        
    input("\nPresiona Enter para continuar...")

def _cambiar_estado():
    clear_screen()
    print_header("CAMBIAR ESTADO DE CITA")
    id_cita = input_int("ID de la cita")
    estado = input("Nuevo estado (PENDIENTE, COMPLETADA, CANCELADA): ").upper()
    
    try:
        CitaService.cambiar_estado(id_cita, estado)
        print("\nEstado actualizado correctamente.")
    except HospitalManagerError as e:
        print(f"\nError: {e}")
    input("\nPresiona Enter para continuar...")

def _eliminar_cita():
    clear_screen()
    print_header("ELIMINAR CITA")
    id_cita = input_int("ID de la cita a eliminar")
    
    try:
        CitaService.eliminar_cita(id_cita)
        print("\nCita eliminada correctamente.")
    except HospitalManagerError as e:
        print(f"\nError: {e}")
    input("\nPresiona Enter para continuar...")

def _medico_mas_citas():
    clear_screen()
    print_header("REPORTE: MÉDICO CON MÁS CITAS")
    try:
        datos = CitaService.obtener_medico_mas_citas()
        if datos:
            print(f"Médico: {datos['nombre']}")
            print(f"Total Citas: {datos['total_citas']}")
        else:
            print("No hay datos suficientes para el reporte.")
    except Exception as e:
        print(f"Error generando reporte: {e}")
    
    input("\nPresiona Enter para continuar...")