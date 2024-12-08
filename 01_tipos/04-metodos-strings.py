""" Metodos Strings """

ANIMAL = " Chanchito Feliz"

# Mostrando todas las letra mayusculas
print(ANIMAL.upper())

# Mostrando todas las letras minusculas
print(ANIMAL.lower())

# Mostrando la primera letra de la primera paalabra en mayuscula
print(ANIMAL.capitalize())

# Mostrando la primera letra de todas las palabras en mayusculas
print(ANIMAL.title())

# Remueve los espacios en blanco que estan a la izquierda y a la derecha del string
print(ANIMAL.strip())

# Busca la posicion de una cadena de caracteres especifico
# #en el string, sino lo encuentra devuelve -1
print(ANIMAL.find("ch"))

# Sustituyendo cadena de caracter dado en el estring
print(ANIMAL.replace("Ch", "L"))

# validando si la cadena de caracteres se encuentra en el string
print("Chan" in ANIMAL)
print("Chan" not in ANIMAL)
