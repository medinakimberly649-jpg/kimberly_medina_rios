# Kimberly Medina Ríos
print("=== Verificación de número par o impar ===")

numero = int(input("Ingresa un número: "))

# Condiciones con AND, OR y NOT
if (numero % 2 == 0 and not numero % 2 != 0) or (numero == 0 and not numero < 0):
    # Caso par
    if numero == 0:
        print(" El número es cero (se considera par)")
    elif numero > 0 and not numero < 0:
        print(" El número es par")
    else:
        print(" El número es par")
else:
    # Caso impar
    if (numero % 2 != 0 and not numero % 2 == 0) or (numero < 0 and not numero > 0):
        if numero > 0:
            print(" El número es impar")
        else:
            print(" El número es impar")