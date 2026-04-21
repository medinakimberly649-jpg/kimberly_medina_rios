# Kimberly Medina Rios
# Ejemplo con BIN, LEN y ROUND

# Número entero
numero = 25

# BIN: convertir a binario
binario = bin(numero)
print(f"El número {numero} en binario es: {binario}")

# LEN: longitud de la cadena binaria (quitando el prefijo '0b')
longitud = len(binario[2:])
print(f"La longitud de la representación binaria de {numero} es: {longitud}")

# ROUND: redondear un número decimal
decimal = 3.14159
redondeado = round(decimal, 2)  # redondea a 2 decimales
print(f"El número {decimal} redondeado a 2 decimales es: {redondeado}")