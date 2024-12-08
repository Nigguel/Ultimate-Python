"""     SETS     """

# significa grupo o conjunto, colección de datos que no se puede repetir y que tampoco está ordenada

PRIMER = {1, 2, 3, 4}

# Añadiendo elemento
PRIMER.add(5)

# Eliminando elemento
PRIMER.remove(1)
print(PRIMER)

SEGUNDO = [3, 4, 5]
SEGUNDO = set(SEGUNDO)
print(SEGUNDO)

# Uniendo sets '|' -> union
print(PRIMER | SEGUNDO)

# interceptando sets '&' -> interseccion
print(PRIMER & SEGUNDO)

# diferencia entre sets '-' -> diferencia
print(PRIMER - SEGUNDO)

# diferencia simetrica '^' -> diferencia simetrica
print(PRIMER ^ SEGUNDO)

if 5 in SEGUNDO:
    print("Hola Mundo")
