from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})

def ListaProducto(request):
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/ListadoProducto.html', {'productos': productos})

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/ListadoProducto.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto_nuevo.html', {'form': form})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/ListadoProducto.html', {'productos': productos})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/ListadoProducto.html', {'productos': productos})
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/producto_nuevo.html', {'form': form})
