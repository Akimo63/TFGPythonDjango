from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title