"""     Seleccionador de clientes     """

# Este ejercicio se enfoca en identificar a los clientes que califican para	una	promoción. Los
# clientes califican si el monto de sus compras	es mayor o igual a 150 dólares.
# Entrada:
#   Un diccionario con:
#       • Claves (str):	IDs	de los clientes.
#       • Valores (float o int): Montos	de las compras.
# Salida:
#   Una	lista con los IDs de los clientes que califican	para la	promoción.


def clientes_seleccionados(clientes: dict) -> list:
    """
    selecciona los clientes que han ganado una promocion de acuerdo a su compra.

    Args:
    clients(dict): diccionario de clientes que verificará si se han ganado una promocion.

    Returns:
    list: Lista de nombre de los clientes que se ganaron una promoción.
    """
    clientes_aceptados = []

    for cliente, monto in clientes.items():
        if monto >= 150:
            clientes_aceptados.append(cliente)

    return clientes_aceptados


compras = {"Cliente1": 200, "Cliente2": 100, "Cliente3": 180}

clientes_promocion = clientes_seleccionados(compras)
print(clientes_promocion)
