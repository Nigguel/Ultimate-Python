"""     Ordenando listas     """

NUMEROS = [2, 4, 1, 45, 75, 22]

# Ordenando listas con el método sort()
NUMEROS.sort()  # Ordena y devuelve la misma lista
print(NUMEROS)

# Ordenando de manera descendente
NUMEROS.sort(reverse=True)
print(NUMEROS)

# Ordenando numeros con la funcion sorted
NUMEROS_2 = sorted(NUMEROS)  # Ordena y crea una lista nueva a partir de la lista pasada
print(NUMEROS_2)

# Ordenando de manera descendente con la función sorted
NUMEROS_2 = sorted(NUMEROS_2, reverse=True)
print(NUMEROS_2)

# Ordenado elementos listas dentro de una lista
USUARIOS = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
USUARIOS.sort()
print(
    USUARIOS
)  # Ordena siempre y cuando el primer elemento de la sublista sea un id o algo que se pueda ordenar


# Ordenando una lista dentro de una lista
USUARIOS = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

USUARIOS.sort(key=lambda el: el[1])  # Utilizando expresiones lambda
print(USUARIOS)
