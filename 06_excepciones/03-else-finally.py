"""     Else - Finally     """

try:
    n1 = int(input("Ingresa primer número: "))
except ValueError as v:
    print("Ocurrió un error!")
else:  # Se ejecuta siempre y cuando no exista ningun error
    print("No ocurrió ningún error")
finally:  # Se ejecuta siempre
    print("se ejecuta siempre")
