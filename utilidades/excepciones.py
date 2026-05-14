class HospitalManagerError(Exception):
    """Excepción base para la aplicación Hospital Manager."""
    pass

class ValidationError(HospitalManagerError):
    """Excepción lanzada cuando hay un error de validación en los datos introducidos."""
    pass

class DatabaseError(HospitalManagerError):
    """Excepción lanzada cuando ocurre un error interactuando con la base de datos."""
    pass

class NotFoundError(HospitalManagerError):
    """Excepción lanzada cuando no se encuentra un recurso solicitado (e.g. paciente no existe)."""
    pass
