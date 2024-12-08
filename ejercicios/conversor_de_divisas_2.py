""" Conversor de Divisas 2 """

# Este programa convierte una cantidad de dinero de una divisa
# a otras.
# Divisas soportadas: USD(dólares estadounidenses),EUR(euros)
# y MXN(pesos mexicanos).
# El usuario ingresa la cantidad y la divisa de origen,y el
# programa calcula las cantidades equivalentes en las otras
# divisas.
# Tasas de Conversión:
#     •1USD=0.95EUR
#     •1USD=20.28MXN
#     •1EUR=21.36MXN

import sys


print("Conversor de Divisas")
CANTIDAD = float(input("Ingrese la cantidad que desea convertir: "))
DIVISA = str(input("Ingrese la divisa de origen (USD, EUR, MXN): ")).upper()

if DIVISA not in ("USD", "EUR", "MXN"):
    print("Divisa de origen no válida.")
    sys.exit()

TASA_USD_EUR = 0.95
TASA_USD_MXN = 20.28
TASA_EUR_MXN = 21.36

if DIVISA == "EUR":
    CANTIDAD_USD = CANTIDAD / TASA_USD_EUR
    CANTIDAD_MXN = CANTIDAD * TASA_EUR_MXN
    print(
        f"""Por la cantidad de {CANTIDAD:.2f} en {DIVISA}
        tendras en al cambio: {CANTIDAD_USD:.2f} UDS o
        {CANTIDAD_MXN:.2f} MXN"""
    )
elif DIVISA == "USD":
    CANTIDAD_EUR = CANTIDAD * TASA_USD_EUR
    CANTIDAD_MXN = CANTIDAD * TASA_USD_MXN
    print(
        f"""Por la cantidad de {CANTIDAD:.2f} en {DIVISA}
        tendras en al cambio: {CANTIDAD_EUR:.2f} EUR o
        {CANTIDAD_MXN:.2f} MXN"""
    )
else:
    CANTIDAD_USD = CANTIDAD / TASA_USD_MXN
    CANTIDAD_EUR = CANTIDAD / TASA_EUR_MXN
    print(
        f"""Por la cantidad de {CANTIDAD:.2f} en {DIVISA}
        tendras en al cambio: {CANTIDAD_USD:.2f} USD o
        {CANTIDAD_EUR:.2f} EUR"""
    )
