# Kimberly Medina Ríos
print("=== Verificación de número positivo o negativo ===")

numero = int(input("Ingresa un número: "))

# Usamos AND, OR y NOT en la condición
if (numero > 0 and not numero < 0) or (numero == 0):
    if numero > 0 and not numero <= 0:
        print("El número es positivo")
    elif numero == 0 or (not numero != 0 and numero == 0):
        print(" El número es cero")
else:
    if numero < 0 and (not numero > 0 or numero != 0):
        print(" El número es negativo")