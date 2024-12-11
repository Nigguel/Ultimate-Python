import csv
import os

# Escribir
# with open("09_archivos/archivo.csv", "w", encoding="utf-8") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "otro twit"])

# Leer
# with open("09_archivos/archivo.csv", encoding="utf-8") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# Actualizar CSV
with open("09_archivos/archivo.csv", encoding="utf-8") as r, open(
    "09_archivos/archivo_temp.csv", "w", encoding="utf-8"
) as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if len(linea) > 0 and linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)

os.remove("09_archivos/archivo.csv")
os.rename("09_archivos/archivo_temp.csv", "09_archivos/archivo.csv")
