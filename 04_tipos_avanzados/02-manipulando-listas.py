"""     Manipulando listas     """

MASCOTAS = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(MASCOTAS[0])

# Remplazando un valor de la lista
MASCOTAS[0] = "Bicho"
print(MASCOTAS)

# Obteniendo parte parcial de la lista
print(MASCOTAS[0:3])
print(MASCOTAS[:2])
print(MASCOTAS[2:])
print(MASCOTAS[-1])
print(MASCOTAS[::2])

NUMEROS = list(range(21))
print(NUMEROS)
print(NUMEROS[::2])  # Numeros PAres
print(NUMEROS[1::2])  # Numeros impares
