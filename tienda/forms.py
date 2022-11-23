from django import forms
from .models import Producto, Compra
import calculation


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'modelo', 'unidades', 'precio', 'detalles', 'marca',)


class CompraForm(forms.ModelForm):
    precio = forms.DecimalField(disabled=True)
    unidades = forms.DecimalField()
    importe = forms.DecimalField(
        widget=calculation.FormulaInput('unidades*precio')
    )
    class Meta:
        model = Compra
        model = Producto
        fields = ('precio',)
