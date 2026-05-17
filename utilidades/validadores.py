import re
from datetime import datetime
from utilidades.excepciones import ValidationError

def validate_dni(dni: str) -> str:
    """Valida el formato de un DNI español (8 números y 1 letra)."""
    dni = dni.strip().upper()
    # Valida solo la estructura, no si la letra corresponde matemáticamente al número
    if not re.match(r'^\d{8}[A-Z]$', dni):
        raise ValidationError("El DNI debe tener 8 dígitos seguidos de una letra (ej: 12345678A).")
    return dni

def validate_telefono(telefono: str) -> str:
    """Valida que el teléfono tenga al menos 9 dígitos."""
    telefono = telefono.strip()
    # Permite "+" opcional y separadores comunes (espacios y guiones)
    if not re.match(r'^\+?[\d\s-]{9,15}$', telefono):
        raise ValidationError("El teléfono debe contener al menos 9 dígitos.")
    return telefono

def validate_fecha_nacimiento(fecha_str: str) -> str:
    """Valida que la fecha tenga formato YYYY-MM-DD y sea en el pasado."""
    fecha_str = fecha_str.strip()
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        if fecha > datetime.now():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return fecha_str
    except ValueError:
        raise ValidationError("La fecha debe tener el formato AAAA-MM-DD (ej: 1990-05-20).")

def validate_fecha_cita(fecha_str: str) -> str:
    """Valida que la fecha de la cita tenga formato YYYY-MM-DD HH:MM y sea en el futuro."""
    fecha_str = fecha_str.strip()
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
        # Alerta: datetime.now() usa la hora del servidor
        if fecha < datetime.now():
            raise ValidationError("La fecha de la cita debe ser en el futuro.")
        return fecha_str
    except ValueError:
        raise ValidationError("La fecha debe tener el formato AAAA-MM-DD HH:MM (ej: 2026-06-01 10:00).")

def validate_not_empty(valor: str, nombre_campo: str) -> str:
    """Valida que un campo no esté vacío."""
    valor = valor.strip()
    # El strip() previo evita que se acepten strings compuestos solo por espacios
    if not valor:
        raise ValidationError(f"El campo '{nombre_campo}' no puede estar vacío.")
    return valor