from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Producto


# Create your views here.
def index(request):
    productos = Producto.objects.all().values()  # pylint: disable=E1101
    # print(productos)
    return JsonResponse(list(productos), safe=False)
