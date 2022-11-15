from django import forms
from .models import Producto, Compra

class ProductoForm(forms.ModelForm):
     class Meta:
        model = Producto
        fields = ('nombre', 'modelo', 'unidades', 'precio', 'detalles', 'marca',)

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('unidades','importe',)

    def clean(self, *args, **kwargs):
        cleaned_data = super(CompraForm, self).clean(*args, **kwargs)
        unidades = cleaned_data.get('unidades')
        if unidades <= Producto.unidades :
            self.add_error('unidades', 'Las unidades deben se igual o menor a las disponibles')
