"""     Conversor de unidades de tiempo     """

# Este ejercicio te	permitirá practicar cómo convertir valores entre diferentes unidades de
# tiempo.Es una excelente oportunidad para trabajar con estructuras condicionales y comprender
# las relaciones entre unidades de tiempo.
# Instrucciones:
#   1. Deine tres funciones:
#       o a_segundos: Convierte	una	cantidad y unidad dada a segundos.
#       o de_segundos: Convierte una cantidad en segundos a otra unidad	deseada.
#       o convertir_tiempo:	Usa	las	dos	funciones anteriores para realizar una conversión completa
#       entre dos unidades.
#   2. Considera las siguientes	unidades:
#   3. segundo,	minuto,	hora, dı́a,	mes	(30	días), año (365días).


def a_segundos(valor: float, unidad: str) -> float | None:
    """
    Convierte una cantidad y unidad dada a segundos.

    Args:
    valor (float): valor a cual se quiere convertir a segundos.
    unidad (str): Unidad del valor.

    Returns:
    float: el valor convertido a segundos.
    """
    if unidad.lower() == "segundos":
        return valor
    if unidad.lower() == "minutos":
        return valor * 60
    if unidad.lower() == "hora":
        return valor * 3600
    if unidad.lower() == "dia":
        return valor * 86400  # Aproximadamente 1 dia
    if unidad.lower() == "mes":
        return valor * 2592000  # Aproximadamente 30 dias
    if unidad.lower() == "año":
        return valor * 31622400  # Aproximadamente 1 año
    return None


def de_segundos(valor_en_segundos: float, unidad: str) -> float | None:
    """
    Convierte una cantidad en segundos a otra unidad deseada.

    Args:
    valor_en_segundos (float): Valor introducido en segundos para convertir a otra unidad.
    unidad (str): Unidad deseada para realizar la conversión.

    Returns:
    float: El valor_en_segundos convertido en la otra unidad deseada
    """
    if unidad.lower() == "segundo":
        return valor_en_segundos
    if unidad.lower() == "minuto":
        return valor_en_segundos / 60
    if unidad.lower() == "hora":
        return valor_en_segundos / 3600
    if unidad.lower() == "dia":
        return valor_en_segundos / 86400  # Aproximadamente 1 dia
    if unidad.lower() == "mes":
        return valor_en_segundos / 2592000  # Aproximadamente 30 dias
    if unidad.lower() == "año":
        return valor_en_segundos / 31622400  # Aproximadamente 1 año
    return None


def convertir_tiempo(
    cantidad: float, unidad_origen: str, unidad_destino: str
) -> float | str | None:
    """
    Se utiliza las otras dos funciones para lograr conseguir uns conversion de tiempo completa

    Args:
    cantidad (float): Cantidad de la unidad que se desea convertir
    unidad_origen (str): Unidad de tiempo del cual se desea convertir
    unidad_destino (Str): Unidad al cual se desea hacer la conversión

    Returns:
    float | str: el numero equivalente a la conversión junto a su unidad

    """
    cantidad_a_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_a_segundos is None:
        return "Unidad de tiempo no válida"
    cantidad_unidad_deseada = de_segundos(cantidad_a_segundos, unidad_destino)
    return f"""
            {cantidad} {unidad_origen}(s) es igual {cantidad_unidad_deseada:.2f} {unidad_destino}(s)
            """


print(convertir_tiempo(2, "hora", "minuto"))
