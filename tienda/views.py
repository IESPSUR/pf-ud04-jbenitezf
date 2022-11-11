from django.shortcuts import render
from django.utils import timezone
from .models import Producto


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})

def ListaProducto(request):
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/ListadoProducto.html', {'productos': productos})
