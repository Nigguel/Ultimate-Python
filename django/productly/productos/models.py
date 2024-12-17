from django.db import models


# Create your models here.
class Categoria(models.Model):
    """
    Modelos Categoria
    """

    nombre = models.CharField(max_length=255)


class Producto(models.Model):
    """
    Modelo Producto
    """

    nombre = models.CharField(max_length=255)
    stock = models.IntegerChoices()
    puntaje = models.FloatField()
    # CASCADE: eliminar el product
    # PROTECT: Lanza un error
    # RESTRICT : Solo elimina si no existen productos
    # SET_NULL: Actualiza a valor nulo
    # SET_DEFAULT: Asigna valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
