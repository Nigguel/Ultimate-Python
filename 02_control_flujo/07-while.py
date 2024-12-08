"""     Ciclo While     """

# NUMERO = 1
# while NUMERO < 100:
#     print(NUMERO)
#     NUMERO *= 2

# COMANDO = ""

# while COMANDO.lower() != "salir":
#     COMANDO = input("$ ")
#     print(COMANDO)

while True:
    COMANDO = input("$ ")
    print(COMANDO)
    if COMANDO.lower() == "salir":
        break
