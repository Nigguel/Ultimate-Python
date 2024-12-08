"""  Comprension de listas  """

USUARIOS = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# NOMBRES = []
# for usuario in USUARIOS:
#     NOMBRES.append(usuario[0])
# print(NOMBRES)

# NOMBRES = [Expresion for item un items]

NOMBRES = [usuario[0] for usuario in USUARIOS]  # -> Map
print(NOMBRES)

# Filtrando en una lista -> Filter
NOMBRES = [usuario for usuario in USUARIOS if usuario[1] > 2]
print(NOMBRES)

# MAP + Filter
NOMBRES = [usuario[0] for usuario in USUARIOS if usuario[1] > 2]
print(NOMBRES)

# Utilizando la función map
NOMBRES = list(map(lambda usuario: usuario[0], USUARIOS))
print(NOMBRES)

# Utilizando la función Filter
MENOS_USUARIOS = list(filter(lambda usuario: usuario[1] > 2, USUARIOS))
print(MENOS_USUARIOS)
