from django.contrib.auth.models import User  # Importar el modelo de usuario
from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=700)
    fabricante = models.CharField(max_length=700)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=750)
    imagen = models.ImageField(upload_to='posters/', null=True)
    favorito = models.BooleanField(default=False)

