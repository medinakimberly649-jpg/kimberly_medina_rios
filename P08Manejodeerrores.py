# Kimberly Medina Rios
def convertir_a_entero(texto):
    try:
        numero = int(texto)
        print(f"Conversión exitosa: {numero}")
    except ValueError:
        print("Error: el texto no se puede convertir a número entero.")

# Ejemplo
convertir_a_entero("123")
convertir_a_entero("hola")