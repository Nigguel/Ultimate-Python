"""     Xargs     """


def suma(*numeros: float) -> float:
    """
    Funcion que suma multiples valores
    """
    resultado = 0
    for i in numeros:
        resultado += i
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(1, 2, 3, 4, 5, 6, 7)
