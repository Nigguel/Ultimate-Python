"""     Funciones     """


def hola() -> str:
    """
    Función que imprime en la terminal un mensaje
    """

    print("Hola Mundo!")
    print("Ultimate Python")


hola()


def saludo_personalizado(nombre: str, apellido="Feliz") -> str:
    """
    Funcion que imprime en la terminal un saludo personalizado
    """
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


saludo_personalizado("Nigguel", "Fernández")

# Argumentos Nombrados
saludo_personalizado(apellido="Fernandez", nombre="Nigguel")
