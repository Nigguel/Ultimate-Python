"""     Ejemplo Real     """


class Model:
    """
    clase model
    """

    TABLA = False

    def __init__(self) -> None:
        if not self.TABLA:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        """
        metodo guardar
        """
        print(f"Guardando {self.TABLA} en BBDD")

    @classmethod
    def buscar_por_id(cls, _id):
        """
        Metodo buscar por id desde la clase
        """
        print(f"Buscando por id {_id} en la tabla {cls.TABLA}")


class Usuario(Model):
    """
    Clase Usuario
    """

    TABLA = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
