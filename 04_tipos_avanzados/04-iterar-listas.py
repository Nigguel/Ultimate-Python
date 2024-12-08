"""     Iterando Listas     """

MASCOTAS = ["Pelusa", "Pulga", "Nigguel", "Chanchito Feliz"]

# mostrando los elementos de una lista a traves de un for
for MASCOTA in MASCOTAS:
    print(MASCOTA)

# Mostrando elemento e indice de una lista a traves de un for
for INDICE, MASCOTA in enumerate(MASCOTAS):
    print(INDICE, MASCOTA)
