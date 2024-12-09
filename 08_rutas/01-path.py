"""     Path     """

from pathlib import Path

# Path(r"C:\Archivos de programa\Minecraft")  #  Ruta absoluta, Usuario window
# Path("/usr/bin")  # Ruta absoluta, Mac, Linux
# Path()  # Crea path en la ruta que nos encontremos
# Path.home()  # Crea path en el home o en el inicio
# Path("one/__init__.py")  # Ruta relativa

path = Path(r"hola-mundo\mi-archivo.py")

path.is_file()
path.is_dir()
path.exists()

print(path.name, path.stem, path.suffix, path.parent, path.absolute())

p = path.with_name("chanchito.py")  # Nos permite cambiar el nombre
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
