"""     Inyeccion de dependencias     """

from pathlib import Path

# import db
# import graphql
# import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "db",
    "api": "api",
    "graphql": "graphql",
}


def load(p):
    """def load"""
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except AttributeError:
        print("El paquete no tiene funcion init")


list(map(load, paths))
