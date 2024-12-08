""" Operadores Lógicos """

# and, or, not

GAS = True
ENCENDIDO = True
EDAD = 18

if GAS and ENCENDIDO:
    print("Puedes avanzar")

if GAS or ENCENDIDO:
    print("Puedes avanzar")

if not GAS or ENCENDIDO:
    print("Puedes avanzar")

if GAS and ENCENDIDO and EDAD > 17:
    print("Puedes avanzar")

if GAS and (ENCENDIDO or EDAD > 17):
    print("Puedes avanzar")

if not GAS and (ENCENDIDO or EDAD > 17):
    print("Puedes avanzar")
