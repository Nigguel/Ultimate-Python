"""     clases     """


class Perro:
    """
    Clase Perro
    """

    def habla(self):  # Métodos
        """
        Función habla
        """
        print("Guau!")


mi_perro = Perro()
mi_perro.habla()
print(isinstance(mi_perro, Perro))
