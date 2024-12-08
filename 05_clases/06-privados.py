"""     Propiedades y métodos privaods     """


class Perro:
    """
    Clase Perro
    """

    def __init__(self, nombre, edad):  # Constructor
        self.__nombre = (
            nombre  # Propiedad privada, se puede acceder solo dentro de la misma clase
        )
        self.edad = edad

    def get_nombre(self):
        """
        Método para acceder a la variable privada de la clase
        """
        return self.__nombre

    def set_nombre(self, nombre):
        """
        Método privado para cambiar el nombre de la propiedad __nombre
        """
        self.__nombre = nombre

    def habla(self):
        """
        Método de clase
        """
        print(f"{self.__nombre} Guau!")

    @classmethod
    def factory(cls):  # Factory Method
        """
        Método de fábrica, crea instancias de la clase
        """
        return cls("Chanchito feliz", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.__dict__)
