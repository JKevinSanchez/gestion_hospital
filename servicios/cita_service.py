from modelos.cita_model import CitaModel
from utilidades.validadores import validate_fecha_cita
from utilidades.excepciones import ValidationError, DatabaseError, NotFoundError

class CitaService:
    @staticmethod
    def crear_cita(id_paciente: int, id_medico: int, fecha: str):
        # Valida que la fecha cumpla con el formato correcto y sea en el futuro
        fecha = validate_fecha_cita(fecha)
        
        # Se delega en el modelo, el cual maneja una transacción para asegurar 
        # la existencia de las claves foráneas (paciente y médico) antes de insertar
        return CitaModel.create_with_transaction(id_paciente, id_medico, fecha)

    @staticmethod
    def listar_citas():
        # Recupera el listado de citas incluyendo datos legibles (ej: nombres de paciente y médico)
        return CitaModel.get_all_with_details()

    @staticmethod
    def cambiar_estado(id_cita: int, estado: str):
        # Actualiza el estado actual de la cita (ej: Pendiente, Completada, Cancelada)
        CitaModel.update_estado(id_cita, estado)

    @staticmethod
    def eliminar_cita(id_cita: int):
        # Solicita la eliminación de la cita; el modelo verifica si el ID existía previamente
        CitaModel.delete(id_cita)

    @staticmethod
    def obtener_medico_mas_citas():
        # Ejecuta una consulta de agregación en el modelo para obtener estadísticas de rendimiento
        return CitaModel.get_medico_con_mas_citas()