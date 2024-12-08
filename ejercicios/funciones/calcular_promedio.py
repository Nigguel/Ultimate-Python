"""     Calcular promedio     """

# En este ejercicio	aprenderás a calcular el promedio de una serie de números. También
# trabajarás con parámetros variables	en	funciones.
# Instrucciones:
#   1. Define una función que acepte un número 1variable de argumentos.
#   2. Si no se	proporcionan números, devuelve	0.
#   3. Si se proporcionan números,	calcula	y devuelve el promedio.


def calcular_promedio(*numeros: float) -> float:
    """
    Función que clacula el promedio de una cantidad de numeros dados.

    Args:
    numeros (float): cantidad de números del cual se quiere saber el promedio.

    Returns:
    float: El promedio de números dados.

    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


# Ejemplo de uso
print(f" El promedio de los números dados es: {calcular_promedio(1, 2, 3, 4, 5):.2f}")
