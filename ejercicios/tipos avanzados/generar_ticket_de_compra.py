"""     Generara ticket de compra     """

# El objetivo de este ejercicio	es crear un programa que genere e imprima un ticket	de compra a
# partir de una lista de productos.	Cada producto está representado por un diccionario con un
# nombre y un precio. El programa debe calcular	la cantidad	de cada producto, el subtotal de cada
# uno y el total de la compra.

# Entrada:
# Una	lista	de	diccionarios con las claves:
#   • 'nombre'	(str):	El nombre del producto.
#   • 'precio'	(float): El	precio del	producto.


def generar_ticket(lista_de_productos: dict) -> str:
    """
    Genera un ticket de compra con un lista de productos, mostrando la cantidad de productos, su
    precio y el total a pagar

    Args:
    lista_de_productos (dict): Lista de productos con su precio

    Returns:
    str: Muestra en la consola un ticket mostrando la cantidad total a pagar y sus productos
    """
    contador_productos = {}
    total = 0

    for producto in lista_de_productos:
        nombre = producto["nombre"]
        if nombre in contador_productos:
            contador_productos[nombre]["cantidad"] += 1
        else:
            contador_productos[nombre] = {"precio": producto["precio"], "cantidad": 1}

    print("-----------------")
    print("Ticket de compra:")
    print("-----------------")
    for nombre, info in contador_productos.items():
        precio = info["precio"]
        cantidad = info["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
        print(f"{nombre} x {cantidad} - ${subtotal:.2f}")

    print("-----------------")
    print(f"Total: ${total:.2f}")
    print("-----------------")


productos = [
    {"nombre": "Manzana", "precio": 0.5},
    {"nombre": "Manzana", "precio": 0.5},
    {"nombre": "Pan", "precio": 1.0},
    {"nombre": "Leche", "precio": 1.5},
]
generar_ticket(productos)
