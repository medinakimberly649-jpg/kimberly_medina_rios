# Kimberly Medina Ríos

# Creamos una lista de frutas
frutas = ["manzana", "plátano", "naranja", "uva"]

# Mostramos la lista completa
print("Lista de frutas:", frutas)

# Accedemos a un elemento por su posición (índice)
print("La primera fruta es:", frutas[0])   # índice 0
print("La última fruta es:", frutas[-1])   # índice -1

# Recorremos la lista con un ciclo for
print("Recorriendo la lista:")
for fruta in frutas:
    print("Fruta:", fruta)

# Agregamos una nueva fruta
frutas.append("mango")
print("Lista después de agregar mango:", frutas)

# Eliminamos una fruta
frutas.remove("plátano")
print("Lista después de eliminar plátano:", frutas)