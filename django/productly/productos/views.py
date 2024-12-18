"""     views.py     """

# from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render


# Create your views here.
def index(request):
    """
    index
    """
    productos = Producto.objects.all()  # pylint: disable=E1101

    return render(request, "index.html", context={"productos": productos})


def detalle(request, producto_id):
    """
    detalle
    """
    producto = Producto.objects.get(id=producto_id)  # pylint: disable=E1101

    return render(request, "detalle.html", context={"producto": producto})
