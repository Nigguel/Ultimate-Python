"""     Ejemplo Real     """

from abc import ABC, abstractmethod


class Model(ABC):
    """
    clase model
    """

    @property
    @abstractmethod
    def tabla(self):
        """
        metodo abstracto tabla
        """

    @abstractmethod
    def guardar(self):
        """
        metodo guardar
        """

    @classmethod
    def buscar_por_id(cls, _id):
        """
        Metodo buscar por id desde la clase
        """
        print(f"Buscando por id {_id} en la tabla {cls.tabla}")


class Usuario(Model):
    """
    Clase Usuario
    """

    tabla = "Usuario"

    def guardar(self):
        print("Guardando Usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
