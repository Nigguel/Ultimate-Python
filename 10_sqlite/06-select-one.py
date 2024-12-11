"""     Select one     """

import sqlite3

with sqlite3.connect("10_sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone())
