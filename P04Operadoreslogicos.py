edad = int(input("Ingresa tu edad: "))
tiene_identificacion = input("¿Tienes identificación? (si/no): ")

if edad >= 18 and tiene_identificacion == "si":
    print("Puedes entrar")
else:
    print("No puedes entrar")