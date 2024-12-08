"""     decorador property     """


class Perro:
    """
    Clase perro
    """

    def __init__(self, nombre) -> dict:
        self.nombre = nombre

    @property  # Trandorma el metodo en una propiedad, solo se trabaja con getter
    def nombre(self):
        """
        metodo para acceder al nombre de la instancia
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """
        metodo que nos permite cambiar un valor
        """
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
perro.nombre = "Joseito"
print(perro.nombre)
