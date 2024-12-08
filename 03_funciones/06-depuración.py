""" Depuración """


def largo(texto) -> int:
    """
    Funcion que muestra cuantos caracteres tiene un string
    """
    resultado = 0
    for _ in texto:
        resultado += 1

    return resultado


print("Chanchito")
L = largo("Hola Mundo")
print(L)
