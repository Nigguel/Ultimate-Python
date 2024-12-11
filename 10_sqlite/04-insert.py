"""     Insert    """

import sqlite3

with sqlite3.connect("10_sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )
