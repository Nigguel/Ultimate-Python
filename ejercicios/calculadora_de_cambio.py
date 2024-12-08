"""     Calculadora de cambio     """

# Este programa calcula el cambio que se debe devolver a un
# cliente después de una compra.

# 1)Solicita al usuario los datos:
#     a)Cantidad de dinero entregado por el cliente.
#     b)Costo del producto.
# 2)Calcula el cambio restando el costo del producto al dinero
# entregado.
# 3)Muestra el cambio a devolver

DINERO_ENTREGADO = input("Ingrese el dinero entregado por el cliente: ")
COSTO_DEL_PRODUCTO = input("Introduzca el costo del producto: ")

DINERO_ENTREGADO = float(DINERO_ENTREGADO)
COSTO_DEL_PRODUCTO = float(COSTO_DEL_PRODUCTO)

CAMBIO = DINERO_ENTREGADO - COSTO_DEL_PRODUCTO

MENSAJE = f"""
El total del cambio es igual a: {CAMBIO}
"""

print(MENSAJE)
