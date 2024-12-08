"""     Diccionarios     """

PUNTO = {"x": 27, "y": 50}
print(PUNTO)

# obtener elemento de un diccionario
print(PUNTO["x"])
print(PUNTO["y"])

# Agregando elemento a un diccionario
PUNTO["Z"] = 45
print(PUNTO)

# Accediendo a los elementos de un diccionario
for valor in PUNTO.items():
    print(valor, end=" ")

for llave in PUNTO:
    print(llave, end=" ")

for valor in PUNTO.values():
    print(valor, end=" ")

# Uso realista de diccionarios en pyton

USUARIOS = [
    {"id": 1, "nombre": "Genesis"},
    {"id": 2, "nombre": "Gabriel"},
    {"id": 3, "nombre": "Luisa"},
    {"id": 4, "nombre": "Nigguel"},
]

for usuario in USUARIOS:
    print(usuario["nombre"])
