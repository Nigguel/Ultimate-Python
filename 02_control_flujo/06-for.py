""" Ciclo for """

for numero in range(5):
    print(numero, numero * "Hola mundo ")

BUSCAR = 10
for numero in range(5):
    print(numero)
    if numero == BUSCAR:
        print("Encontrado", BUSCAR)
        break
else:
    print("No encontre el numero buscado :(")

# Iterando
for char in "Ultimate python":
    print(char)
