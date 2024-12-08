"""     Tuplas     """

# Tuplas, no se modifican
NUMEROS = (1, 2, 3)
print(NUMEROS)

# Sumando tuplas
NUMEROS = (1, 2, 3) + (4, 5, 6)
print(NUMEROS)

# Transformando lista a tuplas
PUNTO = tuple([1, 2])
print(PUNTO)

MENOS_NUMEROS = NUMEROS[:2]
print(MENOS_NUMEROS)

PRIMERO, SEGUNDO, *OTROS = NUMEROS
print(PRIMERO, SEGUNDO, OTROS)

# Iterando tuplas
for n in NUMEROS:
    print(n, end=" ")
