""" Calculadora """

print(
    """Bienvenido a la calculadora
Para salir escribe Salir.
Las operaciones son suma, multi, div y resta"""
)

NUMERO_01 = input("Ingresa un número: ")
NUMERO_01 = int(NUMERO_01)
RESULTADO = 0
while True:
    OPERACION = input("Ingresa operacion: ").lower()
    if OPERACION == "salir":
        break
    NUMERO_02 = input("Ingresa el siguiente número: ")
    NUMERO_02 = int(NUMERO_02)
    if OPERACION == "suma":
        RESULTADO = NUMERO_01 + NUMERO_02

    elif OPERACION == "resta":
        RESULTADO = NUMERO_01 - NUMERO_02

    elif OPERACION == "multi":
        RESULTADO = NUMERO_01 * NUMERO_02

    elif OPERACION == "div":
        RESULTADO = NUMERO_01 / NUMERO_02

    print(f"El resultado es {RESULTADO}")
    NUMERO_01 = RESULTADO
