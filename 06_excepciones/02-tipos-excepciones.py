"""     Tipos de excepciones     """

try:
    N1 = int(input("Ingrese primer número: "))
except ValueError as v:
    print("Ingrese un valor que corresponda")
except NameError as n:
    print("Ocurrio un error")
