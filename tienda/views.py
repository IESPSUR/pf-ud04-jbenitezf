from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CompraForm
from django.utils import timezone


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})

def GestionProducto(request):
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/GestionProducto.html', {'productos': productos})

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/GestionProducto.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto_nuevo.html', {'form': form})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/GestionProducto.html', {'productos': productos})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/GestionProducto.html', {'productos': productos})
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/producto_nuevo.html', {'form': form})

def CompraProducto(request):
    productos = Producto.objects.filter().order_by('nombre')
    return render(request, 'tienda/CompraProducto.html', {'productos': productos})

def producto_comprar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=producto)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.producto = producto
            compra.fecha = timezone.now()
            compra.save()
            producto.unidades = producto.unidades-compra.unidades
            producto.save();
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/CompraProducto.html', {'productos': productos})
    else:
        form = CompraForm(instance=producto)
    return render(request, 'tienda/producto_compra.html', {'form': form})
