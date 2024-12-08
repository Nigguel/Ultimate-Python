""" Palindromo """


def retirar_espacios(texto) -> str:
    """
    Función que elimina los espacios en blanco de un texto
    """
    texto_sin_espacios = ""
    for letra in texto:
        if letra != " ":
            texto_sin_espacios += letra

    return texto_sin_espacios


def volteando_palabra(texto) -> str:
    """
    Funcion que voltea palabras
    """
    palabra_volteada = ""
    for i in range(len(texto) - 1, -1, -1):
        if i != -1:
            palabra_volteada += texto[i]

    return palabra_volteada


def es_palindromo(texto):
    """Funcion que verifica si un texto es palindromo"""
    palabra_sin_espacios = retirar_espacios(texto).lower()
    texto_2 = volteando_palabra(palabra_sin_espacios).lower()
    if palabra_sin_espacios == texto_2:
        return "Es palindromo"

    return "No es palindromo"


print("Amo la paloma", es_palindromo("Amo la paloma"))
