"""     Herencia     """


class Animal:
    """
    Clase animal
    """

    def comer(self):
        """
        Metodo comer
        """
        print("comer")


class Perro(Animal):
    """
    Clase perro
    """

    def pasear(self):
        """
        Metodo pasear
        """
        print("paseando")


class Chanchito(Perro):
    """
    Clase Chanchito
    """

    def programar(self):
        """
        metodo programar
        """
        print("Programando")


perro = Perro()
perro.comer()
Chanchito = Chanchito()
Chanchito.comer()
