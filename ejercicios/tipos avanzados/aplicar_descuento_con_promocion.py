"""     Aplicar descuento con promoción     """

# En este ejercicio, además de	identificar	a los clientes que califican para la promoción, se	les
# aplica un	descuento del 10%.
# El programa	retorna:
#   1. Una lista con los IDs de	los	clientes que califican.
#   2. Un diccionario con los IDs de los clientes y sus	montos ajustados después del descuento.
# Entrada:
# Un diccionario donde:
#   • Claves (str):	IDs	de	los	clientes.
#   • Valores (float o int): Montos	de	las	compras.
# Salida:
# Dos	elementos:
#   1. Lista de	IDs	de los	clientes elegibles.
#   2. Diccionario	con	los	montos	ajustados.


def aplicar_promocion(clientes: dict) -> dict | list:
    """
    asdf
    """
    lista_clientes = []
    descuento_clientes = {}

    for cliente, compra in clientes.items():
        if compra >= 150:
            lista_clientes.append(cliente)
            descuento_clientes[cliente] = compra - (compra * 0.1)

    return lista_clientes, descuento_clientes


compras = {"Cliente1": 200, "Cliente2": 100, "Cliente3": 180}

resultado = aplicar_promocion(compras)
print(resultado)
