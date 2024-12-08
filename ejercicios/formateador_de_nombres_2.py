"""     Formateador de nombres 2     """

# Este programa solicita al usuario su nombre completo y lo
# formatea eliminando espacios adicionales y capitalizando las
# palabras.
# Se asegura de que el usuario ingrese un nombre y un apellido
# válidos antes de proceder.
# Variables:
#     •nombre(str): Primer nombre del usuario.
#     •segundo_nombre(str): Segundo nombre del usuario(opcional).
#     •primer_apellido(str): Primer apellido del usuario.
#     •segundo_apellido(str): Segundo apellido del usuario(opcional).
#     •nombre_completo(str):Nombre completo concatenado y formateado.

PRIMER_NOMBRE = input("Escriba su primer nombre: ").strip().capitalize()
while not PRIMER_NOMBRE or PRIMER_NOMBRE == "exit":
    print("No ingresaste tu primer nombre, por favor intente nuevamente.")
    PRIMER_NOMBRE = input("Escriba su primer nombre: ").strip().capitalize()

SEGUNDO_NOMBRE = input("Escriba su segundo nombre (opcional): ").strip().capitalize()

PRIMER_APELLIDO = input("Escriba su primer apellido: ").strip().capitalize()
while not PRIMER_APELLIDO or PRIMER_APELLIDO == "exit":
    print("No ingresaste tu primer apellido, por favor intente nuevamente.")
    PRIMER_APELLIDO = input("Escriba su primer apellido: ").strip().capitalize()

SEGUNDO_APELLIDO = input(
    "Escriba su segundo apellido (opcional): ".capitalize().strip()
)

MENSAJE = (
    f"{PRIMER_NOMBRE} {SEGUNDO_NOMBRE} {PRIMER_APELLIDO} {SEGUNDO_APELLIDO}".replace(
        "  ", " "
    )
)

print(MENSAJE)
