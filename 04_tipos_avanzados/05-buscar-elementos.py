""" Buscando elementos"""

MASCOTAS = ["Pelusa", "Pulga", "Nigguel", "Wolfgang", "Chanchito Feliz"]

# Buscando un elemento
if "Wolfgang" in MASCOTAS:
    print(MASCOTAS.index("Wolfgang"))
else:
    print("No existe ese nombre en la lista")
