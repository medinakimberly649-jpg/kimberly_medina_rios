# Kimberly Medina Rios
import math

def calcular_raiz(numero):
    try:
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {resultado}")
    except ValueError:
        print("Error: no se puede calcular la raíz cuadrada de un número negativo.")

# Ejemplo
calcular_raiz(16)
calcular_raiz(-9)