"""     Operador desempaquetar     """

# Desempaquetar listas
LISTA_1 = [1, 2, 3, 4]
print(LISTA_1)
print(*LISTA_1)

# Desempaquetar Tuplas
TUPLA = (1, 2, 3, 4)
print(TUPLA)
print(*TUPLA)

LISTA_2 = [5, 6]

# Creando una nueva lista con las listas existentes
COMBINADA = ["Hola", *LISTA_1, "Mundo", *LISTA_2]
print(COMBINADA)


# Desempaquetar Diccionarios
PUNTO_1 = {"x": 1}
PUNTO_2 = {"y": 2}

# Creando nuevo diccionario con los diccionarios existentes
NUEVO_PUNTO = {**PUNTO_1, **PUNTO_2, "Z": "Mundo"}
print(NUEVO_PUNTO)
