print("=== Verificación de edad ===")

edad = int(input("Ingresa tu edad: "))

# Usamos AND, OR y NOT
if (edad >= 18 and edad <= 99) or (not edad < 0):
    if edad >= 18 and not edad < 18:
        print(" Eres mayor de edad")
    elif edad < 18 and (edad >= 0 or not edad < 0):
        print(" Eres menor de edad")
else:
    print(" Edad inválida (no puede ser negativa o mayor a 99)")