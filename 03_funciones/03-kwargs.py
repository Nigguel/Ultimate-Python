"""     Kwargs     """


def get_product(**datos):
    """Kwards"""
    print(datos["id"], datos["name"])


get_product(id="23", name="iPhone", desc="Esto es un iphone")
