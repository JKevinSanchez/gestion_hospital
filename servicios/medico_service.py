from modelos.medico_model import MedicoModel
from utilidades.validadores import validate_not_empty
from utilidades.excepciones import ValidationError, DatabaseError, NotFoundError

class MedicoService:
    @staticmethod
    def crear_medico(nombre: str, especialidad: str):
        # Valida que los campos obligatorios no estén vacíos antes de proceder
        nombre = validate_not_empty(nombre, "Nombre")
        especialidad = validate_not_empty(especialidad, "Especialidad")
        
        # Delega la inserción en la base de datos tras asegurar la integridad de los datos
        return MedicoModel.create(nombre, especialidad)

    @staticmethod
    def listar_medicos():
        # Recupera todos los médicos registrados del modelo
        return MedicoModel.get_all()

    @staticmethod
    def actualizar_medico(id_medico: int, nombre: str, especialidad: str):
        # Asegura que las modificaciones cumplan con las restricciones de campos obligatorios
        nombre = validate_not_empty(nombre, "Nombre")
        especialidad = validate_not_empty(especialidad, "Especialidad")
        
        # Aplica los cambios; si el id_medico no existe, el modelo lanzará NotFoundError
        MedicoModel.update(id_medico, nombre, especialidad)

    @staticmethod
    def eliminar_medico(id_medico: int):
        # Solicita la eliminación del registro; el modelo valida si el ID realmente existía
        MedicoModel.delete(id_medico)