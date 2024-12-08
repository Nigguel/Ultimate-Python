"""     Constructor de una clase     """


class Perro:
    """
    Clase Perro
    """

    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    def habla(self):  # Métodos
        """
        Función habla
        """
        print(f"{self.nombre} dice:Guau!")


mi_perro = Perro("Carlos", 2)

mi_perro.habla()
