"""     Caja Registradora     """

# Este programa simula una caja registradora que acumula el
# precio de los productos ingresados por el usuario.

TOTAL = 0

while True:
    PRECIO = input("Escriba el precio del producto (escriba fin para terminar): ")
    if PRECIO.lower() == "fin":
        break

    TOTAL += float(PRECIO)

print(f"El total a pagar es {TOTAL:.2f}$")
