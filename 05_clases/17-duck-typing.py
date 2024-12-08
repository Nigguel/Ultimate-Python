"""     Duck Typing     """


class Usuario:
    """
    Clase Usuario
    """

    def guardar(self):
        print("Guardando en BBDD")


class Sesion:
    """
    clase Sesion
    """

    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    """
    funcion guardar aplicando polimorfismo
    """
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
