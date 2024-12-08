"""     Filas en Python     """

# Filas -> FIFO = First in First out

from collections import deque


FILA = deque([1, 2])

# Agregando elementos
FILA.append(3)
FILA.append(4)
FILA.append(5)
FILA.append(6)
print(FILA)

# Eliminando elementos de la fila
FILA.popleft()
print(FILA)

# Verificar si la lista esta vacia
if not FILA:
    print("Fila vacia")
