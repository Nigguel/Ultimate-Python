"""     Lectura y escritura     """

from pathlib import Path

archivo = Path("09_archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0, "Hola mundo!")
archivo.write_text("\n".join(texto), "utf-8")
