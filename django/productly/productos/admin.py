from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    """
    Personalizando el modelo de categoria
    """

    list_display = ["id", "nombre"]


class ProductoAdmin(admin.ModelAdmin):
    """
    Personalizando el modelo de Producto
    """

    exclude = ("creado_en",)
    list_display = ["id", "nombre", "stock", "creado_en"]


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
