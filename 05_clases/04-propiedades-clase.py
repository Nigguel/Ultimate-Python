"""     Propiedades de clases     """


class Perro:
    """
    Clase Perro
    """

    PATAS = 4

    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    def habla(self):  # Métodos
        """
        Función habla
        """
        print(f"{self.nombre} dice:Guau!")


Perro.PATAS = 3  # Modifica la variable para todas las instacias de la clase
mi_perro = Perro("Carlos", 2)
mi_perro.PATAS = 5  # Modifica la variable solo para esa instancia de la clase
mi_perro2 = Perro("Felipe", 2)

print(Perro.PATAS)
print(mi_perro.PATAS)
