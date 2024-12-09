"""    Directorios     """

from pathlib import Path

path = Path("rutas")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos = [p for p in path.glob("01-*.py")]  # Seleccionar archivos por un patron
print(archivos)

archivos = [
    p for p in path.rglob("*.py")
]  # incluye todos los archivos de manera recursiva
print(archivos)
