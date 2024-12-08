"""     Conversor de Divisas     """

#    Este programa calcula cuánto costaría un producto en
# diferentes monedas extranjeras a partir de una cantidad
# ingresada en moneda local.

#    1)Solicita al usuario que ingrese una cantidad en su
#      moneda local.
#    2)Convierte la cantidad a las siguientes monedas:
#       a) USD: cantidad * 0.050
#       b) EUR: cantidad * 0.047
#       c) GBP: cantidad * 0.039
#       d) JPY: cantidad * 7.71
#    3)Muestra los resultados de cada conversión

MONEDA_LOCAL = input("Ingrese la cantidad de la moneda local: ")

MONEDA_LOCAL = float(MONEDA_LOCAL)
USD = MONEDA_LOCAL * 0.050
EUR = MONEDA_LOCAL * 0.047
GBP = MONEDA_LOCAL * 0.039
JPY = MONEDA_LOCAL * 7.71

MENSAJE = f"""
El valor de la moneda local convertidas en otras monedas es:
    USD: {USD:.2f}
    EUR: {EUR:.2f}
    GBP: {GBP:.2f}
    JPY: {JPY:.2f}
"""

print(MENSAJE)
