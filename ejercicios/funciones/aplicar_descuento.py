"""     Aplicar descuento     """

# Este ejercicio tiene como	objetivo ayudarte a comprender
# cómo	calcular el	total de una cuenta	después de	aplicar	un
# descuento. Es	ideal para practicar operaciones matemáticas
# simples y	trabajar con funciones.
# Instrucciones:
#   1. Define una función que tome como parámetros el total de
#      una cuenta y	un porcentaje de descuento.
#   2. Calcula el monto	correspondiente	al descuento.
#   3. Resta el	descuento del total	original.
#   4. Devuelve	el total final.


def aplicando_descuento(valor_de_la_cuenta: float, porcentaje: float) -> float:
    """
    Función que calcula el total de una compra aplicando un
    descuento.

    Args:
    valor_de_la_cuenta (float): El total de la compra
    porcentaje (float): El descuento aplicado al total de la
    compra

    Returns:
    float: El total de la compra con el descuento aplicado

    """

    descuento = valor_de_la_cuenta * (porcentaje / 100)
    total = valor_de_la_cuenta - descuento
    return total


TOTAL = 1000
DESCUENTO = 20
TOTAL_A_PAGAR = aplicando_descuento(TOTAL, DESCUENTO)
print(
    f"El total de la cuenta aplicando un descuento del {DESCUENTO}% es de {TOTAL_A_PAGAR:.2f}$"
)
