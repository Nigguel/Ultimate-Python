""" Ejercicios """

# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes.


def eliminar_espacios(string) -> list:
    """
    Funcion que elimina los espacios en blanco de un string
    """
    string_sin_espacios = [letra for letra in string if letra != " "]
    return string_sin_espacios


# 2. Contar en un diccionario cuanto se repiten los caracteres de un string.


def cuenta_chars(lista) -> dict:
    """
    Funcion que cuanta la cantidad de letras que se repiten en una lista
    y los guarda en un diccionario
    """
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


# 3. Ordenar las llaves de un diccionario por el valor que
# tiene y devolver una lista que contiene tuplas


def ordenar(diccionario) -> list:
    """
    Funcion que ordena las llaves de un diccionario y lo devuelve en una lista
    """
    return sorted(diccionario.items(), key=lambda key: key[1], reverse=True)


# 4. De un listado de Tuplas, devolver las tuplas que tenga el mayor valor


def mayores_tuplas(lista):
    """
    Función que devuelve las tuplas que tenga el mayor valor de un listado de tuplas
    """
    maximo = lista[0][1]
    repuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        repuesta[orden[0]] = orden[1]

    return repuesta


# 5. Crear un mensaje qu diga: Los caracteres que más se repiten con {} repeticiones son: -{}, -{}


def crea_mensaje(diccionario):
    """
    Función que devuelve un mensaje con los caracteres que mas se repiten
    """
    mensaje_1 = "Los que más se repiten son:\n"

    for key, valor in diccionario.items():
        mensaje_1 += f"- {key} con {valor} repeticiones\n"

    return mensaje_1


palabra = eliminar_espacios("Hola mundo este es mi string")
cuenta_letra = cuenta_chars(palabra)
ordenados = ordenar(cuenta_letra)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
