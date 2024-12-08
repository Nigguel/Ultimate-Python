""" Colas en Python """

# Colas -> LIFO = Last in First out

PILA = []
PILA.append(1)
PILA.append(2)
PILA.append(3)
print(PILA)


ULTIMO_ELEMENTO = PILA.pop()
print(ULTIMO_ELEMENTO)
print(PILA)

print(PILA[-1])

PILA.pop()
PILA.pop()

if not PILA:
    print("Pila vacia")
