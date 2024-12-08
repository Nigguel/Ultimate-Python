"""     Metodos de clases     """


class Perro:
    """
    Clase Perro
    """

    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    # Se hace para si es algo común entre las instacias de la clase
    @classmethod
    def habla(cls):  # Métodos de clase
        """
        Método de clase
        """
        print("Guau!")

    @classmethod
    def factory(cls):  # Factory Method
        """
        Métopdo de fábrica, crea instancias de la clase
        """
        return cls("Chanchito feliz", 4)


Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Carlos", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
