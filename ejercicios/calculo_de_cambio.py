"""     Calculo de cambio     """

# Este programa calcula el cambio que debe darse al cliente
# según el pago y el total de la cuenta.

import sys


TOTAL = input("Por favor ingrese el total de la cuenta: ")
PAGO = input("Por favor ingrese la cantidad de pago: ")

TOTAL = float(TOTAL)
PAGO = float(PAGO)

if TOTAL < 0 or PAGO < 0:
    print("El total de la cuenta y el pago debe ser mayor a 0")
    sys.exit()

if PAGO == TOTAL:
    print("El cliente ha pagado la misma cantidad del total. No se requiere cambio")
elif PAGO < TOTAL:
    DIFERENCIA = TOTAL - PAGO
    print(f"El cliente ha pagado menos. Faltan {DIFERENCIA}$")
else:
    DIFERENCIA = PAGO - TOTAL
    print(f"El cliente ha pagado de más. El cambio es de {DIFERENCIA}$")
