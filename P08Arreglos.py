# Kimberly Medina Ríos
def acceder_lista(lista, indice):
    try:
        print(f"Elemento en posición {indice}: {lista[indice]}")
    except IndexError:
        print("Error: el índice está fuera del rango de la lista.")

# Ejemplo
numeros = [10, 20, 30]
acceder_lista(numeros, 1)   # válido
acceder_lista(numeros, 5)   # error