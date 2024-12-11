"""     Creando tablas     """

import sqlite3

con = sqlite3.connect("10_sqlite/app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit()
con.close()