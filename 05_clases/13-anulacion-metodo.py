"""     Anulacioin de métodos     """


class Ave:
    """
    Clase Ave
    """

    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        """
        Metodo vuela
        """
        print("Vuela ave")


class Pato(Ave):
    """
    pato
    """

    def __init__(self):
        super().__init__()
        self.nada = "nadador"

    def vuela(self):
        print("Vuela Pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
