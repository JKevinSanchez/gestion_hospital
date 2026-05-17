import os

def clear_screen():
    """Limpia la pantalla de la consola (compatible con Windows y Linux/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title: str):
    """Imprime un encabezado con formato ASCII simple."""
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50 + "\n")

def input_with_validation(prompt: str, validation_func, default=None):
    """
    Solicita un input al usuario y aplica una función de validación.
    Sigue pidiendo hasta que sea válido o cancele.
    """
    while True:
        try:
            prompt_str = f"{prompt} [{default}]: " if default else f"{prompt}: "
            valor = input(prompt_str)
            if default and not valor.strip():
                return default
            return validation_func(valor)
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Inténtalo de nuevo. (Presiona Ctrl+C para cancelar)\n")

def input_int(prompt: str) -> int:
    """Solicita un entero al usuario de forma segura."""
    while True:
        try:
            return int(input(f"{prompt}: "))
        except ValueError:
            print("Error: Debes introducir un número entero válido.\n")

def print_table(headers: list, rows: list):
    """
    Imprime una tabla de manera formateada en la consola.
    """
    if not rows:
        print("No hay datos para mostrar.\n")
        return

    # Calcular el ancho máximo de cada columna
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Formato de fila
    row_format = " | ".join([f"{{:<{w}}}" for w in col_widths])
    
    separator = "-" * (sum(col_widths) + len(col_widths) * 3 - 1)
    print(separator)
    print(row_format.format(*headers))
    print(separator)
    
    for row in rows:
        print(row_format.format(*[str(c) for c in row]))
        
    print(separator + "\n")
