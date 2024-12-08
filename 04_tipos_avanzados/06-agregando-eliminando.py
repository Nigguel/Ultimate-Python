""" Agregando y eliminando datos en una lista """

MASCOTAS = ["Wolfgang", "Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito Feliz"]
print(MASCOTAS)

# Agregando mascota
MASCOTAS.insert(1, "Melvin")
print(MASCOTAS)

MASCOTAS.append("Chanchito Triste")
print(MASCOTAS)


# Eliminando elementos
MASCOTAS.remove("Pulga")
print(MASCOTAS)

MASCOTAS.pop()  # Eliminando el ultimo elemento de una lista
print(MASCOTAS)

MASCOTAS.pop(1)  # Eliminando utilizando el indice
print(MASCOTAS)

del MASCOTAS[0]
print(MASCOTAS)

MASCOTAS.clear()
print(MASCOTAS)
