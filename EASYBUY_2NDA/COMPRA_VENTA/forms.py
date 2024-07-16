from django import forms
from COMPRA_VENTA.models import Producto

class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'fabricante', 'precio', 'descripcion', 'imagen']
        labels = {
            'nombre_producto': 'Producto', 
            'fabricante': 'Fabricante',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
            'imagen': 'Imagen'
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

