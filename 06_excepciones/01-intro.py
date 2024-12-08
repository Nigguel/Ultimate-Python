"""     Introduccion a Excepciones     """

try:
    N1 = int(input("Ingrese primer número: "))
except ValueError:
    print("Ocurrio un error")
