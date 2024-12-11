"""     Archivos Json     """

import json
from pathlib import Path

# Escribir Json
# PRODUCTOS = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(PRODUCTOS)
# Path("09_archivos/productos.json").write_text(data, encoding="utf-8")

# Leer Json
data = Path("09_archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
# print(productos)

# modificar Json
productos[0]["name"] = "Chanchito feliz"
Path("09_archivos/productos.json").write_text(json.dumps(productos), encoding="utf-8")
