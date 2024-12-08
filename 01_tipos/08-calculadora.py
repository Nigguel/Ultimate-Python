""" Calculadora """

N1 = input("Ingresa el primer número: ")
N2 = input("Ingresa el segundo número: ")

N1 = int(N1)
N2 = int(N2)

SUMA = N1 + N2
RESTA = N1 - N2
MULTIPLICACION = N1 * N2
DIVISION = N1 / N2

MENSAJE = f"""
Para los números {N1} y {N2}:
    El resultado de la suma ({N1} + {N2}) es {SUMA}
    El resultado de la resta ({N1} - {N2}) es {RESTA}
    El resultado de la multiplicación ({N1} * {N2}) es {MULTIPLICACION}
    El resultado de la división ({N1} / {N2}) es {DIVISION}
"""

print(MENSAJE)
