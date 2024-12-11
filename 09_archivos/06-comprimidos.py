"""     Archivos comprimidos     """

from pathlib import Path
from zipfile import ZipFile

with ZipFile(
    "09_archivos/comprimidos.zip",
    "w",
) as archivo_zip:
    # curso-py
    for path in Path("09_archivos").rglob("*.*"):
        if str(path) != "09_archivos/comprimidos.zip":
            archivo_zip.write(path, path.relative_to("09_archivos"))

with ZipFile("09_archivos/comprimidos.zip") as archivo_zip:
    # print(archivo_zip.namelist())
    info = archivo_zip.getinfo("09_archivos/06-comprimidos.py")
    print(info.file_size, info.compress_size)
