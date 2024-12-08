"""     Herencia multiple     """


class Caminador:
    """
    Clase caminador
    """

    def caminar(self):
        """
        Metodo caminar
        """
        print("caminando")


class Volador:
    """
    Clase volador
    """

    def volar(self):
        """
        Metodo volar
        """
        print("volando")


class Nadador:
    """
    Clase Nadador
    """

    def nadar(self):
        """
        Método nadar
        """
        print("Nadando")


class Pato(Volador, Nadador, Caminador):
    """
    Clase Pato
    """

    def programar(self):
        """
        Método programador
        """
        print("Programando")
