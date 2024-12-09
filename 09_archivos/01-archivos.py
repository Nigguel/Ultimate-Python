"""     Archivos     """

from pathlib import Path
from time import ctime

archivo = Path("09_archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())

print("acesso", ctime(archivo.stat().st_atime))  # Timestamp (1970) Unix
print("creación", ctime(archivo.stat().st_birthtime))
print("modificación", ctime(archivo.stat().st_mtime))
