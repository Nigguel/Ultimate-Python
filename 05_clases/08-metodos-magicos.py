"""     Métodos magicos     """


class Perro:
    """
    Clase Perro
    """

    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    def __del__(self):  # Destructor
        """
        destructor
        """
        print(f"Chao perro :( {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):  # Métodos
        """
        Función habla
        """
        print(f"{self.nombre} dice:Guau!")


perro = Perro("Chanchito", 5)
del perro
