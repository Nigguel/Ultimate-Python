"""     Verificación de tweets     """

# Este programa solicita alusuario que ingrese un tweet
# y verifica si cumple con el limite de 20 caracteres.
#   •Si el tweet excede los 20 caracteres, muestra un mensaje
#   indicando que se ha sobrepasado el límite.
#   •Si el tweet tiene 20 caracteres o menos, indica que el tweet
#   ha sido publicado.
#   •No se aceptan tweets vacios

TWEET = input("Ingrese su tweet: ")

if not TWEET:
    print("No se puede publicar un tweet vacío")
elif len(TWEET) > 20:
    print("Ha sobrepasado el límite de su publicación")
else:
    print("Su tweet ha sido publicado")
