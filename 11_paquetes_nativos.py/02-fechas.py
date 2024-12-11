"""     Fechas     """

import time
from datetime import datetime

print(time.time())

fecha = datetime(2024, 12, 4)
print(fecha)

ahora = datetime.now()
print(ahora)

fechaStr = datetime.strptime("2024/11/14", "%Y/%m/%d")
print(fechaStr)

print(fecha.strftime("%Y.%m.%d"))

print(fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute, fecha.second)
