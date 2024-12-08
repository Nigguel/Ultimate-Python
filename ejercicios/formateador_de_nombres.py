"""     Formateador de Nombres     """

# Este programa asegura que los nombres ingresados por el
# usuario estén correctamente formateados:

#     1)Solicita al usuario los siguientes datos:
#         a)Primer nombre.
#         b)Segundo nombre (opcional).
#         c)Primer apellido.
#         d)Segundo apellido(opcional).
#     2)Elimina espacios innecesarios y capitaliza la primera
#     letra de cada palabra .
#     3)Combina todos los nombres y apellidos en un nombre
#     completo correctamente formateado.

PRIMER_NOMBRE = input("Primer nombre: ").strip().capitalize()
SEGUNDO_NOMBRE = input("Segundo nombre: ").strip().capitalize()
PRIMER_APELLIDO = input("Primer apellido: ").strip().capitalize()
SEGUNDO_APELLIDO = input("Segundo apellido: ").strip().capitalize()

NOMBRE_COMPLETO = (
    f"{PRIMER_NOMBRE} {SEGUNDO_NOMBRE} {PRIMER_APELLIDO} {SEGUNDO_APELLIDO}".replace(
        "  ", " "
    )
)

print(NOMBRE_COMPLETO)
