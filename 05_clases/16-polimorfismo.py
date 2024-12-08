"""     Polimorfismo     """

from abc import ABC, abstractmethod


class Model(ABC):
    """
    Clase Model
    """

    @abstractmethod
    def guardar(self):
        """
        Metodo abstracto guardar
        """


class Usuario(Model):
    """
    Clase Usuario
    """

    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model):
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
