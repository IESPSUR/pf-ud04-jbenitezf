from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Compra, Marca
from .forms import ProductoForm, CompraForm
from django.utils import timezone
from django.db.models import Sum


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

def saber_mas(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/saber_mas.html', {'producto' : producto})
def producto_comprar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=producto)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            importe = form.cleaned_data['importe']

            if producto.unidades < unidades :
                return redirect('producto_comprar',pk)
            else:
                Compra.objects.create(fecha=timezone.now(), importe=importe, unidades=unidades, producto=producto)
                producto.unidades = producto.unidades-unidades
                producto.save();
                return redirect('checkout', pk);

    else:
        form = CompraForm(instance=producto)
    return render(request, 'tienda/producto_compra.html', {'form': form})

def checkout(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/checkout.html', {'producto' : producto})

def informes(request):
    return render(request, 'tienda/informes.html')

def marcas(request):
    marca = Marca.objects.filter().order_by('nombremarca')
    return render(request, 'tienda/Marcas.html', {'marca': marca})

def productos_in_marcas(request, nombremarca):
    producto = Producto.objects.all().filter(marca__nombremarca=nombremarca)
    return render(request, 'tienda/Informe_marca.html', {'productos': producto})

def top_ten(request):
    producto = Compra.objects.values('producto__nombre').annotate(unidades=Sum('unidades')).order_by('-unidades')[:10]
    productos = list(producto)

    return render(request, 'tienda/top_ten.html', {'productos': productos})
