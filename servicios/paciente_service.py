from modelos.paciente_model import PacienteModel
from utilidades.validadores import validate_dni, validate_telefono, validate_fecha_nacimiento, validate_not_empty
from utilidades.excepciones import ValidationError, DatabaseError, NotFoundError

class PacienteService:
    @staticmethod
    def crear_paciente(nombre: str, dni: str, telefono: str, fecha_nacimiento: str):
        # Primero se ejecutan todas las validaciones de formato y negocio; si alguna falla, interrumpe el flujo
        nombre = validate_not_empty(nombre, "Nombre")
        dni = validate_dni(dni)
        telefono = validate_telefono(telefono)
        fecha_nacimiento = validate_fecha_nacimiento(fecha_nacimiento)

        # Si los datos son válidos, se delega la persistencia de forma segura en la base de datos
        return PacienteModel.create(nombre, dni, telefono, fecha_nacimiento)

    @staticmethod
    def listar_pacientes():
        # Recupera la lista completa de pacientes mapeados directamente a diccionarios
        return PacienteModel.get_all()
        
    @staticmethod
    def obtener_paciente(id_paciente: int):
        # Retorna el paciente o propaga la excepción NotFoundError si el ID no existe
        return PacienteModel.get_by_id(id_paciente)

    @staticmethod
    def actualizar_paciente(id_paciente: int, nombre: str, telefono: str, fecha_nacimiento: str):
        # Valida los datos modificados antes de aplicar los cambios en el registro
        nombre = validate_not_empty(nombre, "Nombre")
        telefono = validate_telefono(telefono)
        fecha_nacimiento = validate_fecha_nacimiento(fecha_nacimiento)
        
        # Actualiza el registro; si el id_paciente no existe, lanzará NotFoundError desde el modelo
        PacienteModel.update(id_paciente, nombre, telefono, fecha_nacimiento)

    @staticmethod
    def eliminar_paciente(id_paciente: int):
        # Ejecuta la baja del paciente; el modelo se encarga de verificar la existencia previa del ID
        PacienteModel.delete(id_paciente)