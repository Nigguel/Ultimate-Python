"""     Open     """

from io import open

# Escritura
# TEXTO = "Hola Mundo!"

# with open("09_archivos/hola-mundo.txt", "w", encoding="utf-8") as archivo:
#     archivo.write(TEXTO)

# Lectura
# with open("09_archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.read())


# Lectura como lista
# with open("09_archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.readlines())

# with y seek
# with open("09_archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.readlines())
#     archivo.seek(
#         0
#     )  # Mueve el puntero a una posicion especifica, ene este caso a la posicion inicial
#     for linea in archivo:
#         print(linea)

# Agregar
# with open("09_archivos/hola-mundo.txt", "a+", encoding="utf-8") as archivo:
#     archivo.write("\nChao mundo!")

# Lectura y Escritura
with open("09_archivos/hola-mundo.txt", "r+", encoding="utf-8") as archivo:
    TEXTO = archivo.readlines()
    archivo.seek(0)
    TEXTO[0] = "Chanchito feliz"
    archivo.writelines(TEXTO)
