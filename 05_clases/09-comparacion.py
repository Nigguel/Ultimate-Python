"""     Comparación entre objetos     """


class Coordenadas:
    """
    Clase coordenada
    """

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Metodo magico que verifica si 2 objetos son iguales
    def __eq__(self, otro: object) -> bool:
        return self.lat == otro.lat and self.lon == otro.lon

    # Metodo magico que verifica si un objeto es mayor a otro
    def __lt__(self, otro: object) -> bool:
        return self.lat + self.lon < otro.lat + otro.lon

    # Metodo magico que verifica si un objeto es mayor o igual a otro

    def __le__(self, otro: object) -> bool:
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)
print(coords >= coords2)
