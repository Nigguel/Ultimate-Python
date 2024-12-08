"""     Conversor de Temperatura     """

#     Este programa convierte una temperatura dada en grados
# Celsius a dos escalas diferentes en: Fahrenheit y Kelvin.

#     1)Pide al usuario que ingrese una temperatura en grados
#     Celsius.
#     2)Realiza las siguientes conversiones:
#         a)Celsius a Fahrenheit: (grados Celsius * 9/5) + 32
#         b)Celsius a Kelvin: grados Celsius + 273.15
#     3)Muestra las temperaturas convertidas en ambas escalas.

GRADOS_CELSIUS = input("Ingrese el valor de grados Celsius: ")

GRADOS_CELSIUS = float(GRADOS_CELSIUS)
GRADOS_FAHRENHEIT = (GRADOS_CELSIUS * 9 / 5) + 32
GRADOS_KELVIN = GRADOS_CELSIUS + 273.15

MENSAJE = f"""
    Grados Celcius: {GRADOS_CELSIUS} C°
    Grados Fahrenheit: {GRADOS_FAHRENHEIT} F°
    Grados Kelvin: {GRADOS_KELVIN:.2f} K°
"""

print(MENSAJE)
