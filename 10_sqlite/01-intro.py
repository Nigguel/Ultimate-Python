"""     Introducción a sqlite     """

import sqlite3

# Conectandose a la base de datos
con = sqlite3.connect("10_sqlite/app.db")
con.close()  # Agregar siempre
