from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KILOGRAMO = 'kg', 'Kilogramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.CharField(max_length=3, choices=ProductUnits.choices, default=ProductUnits.UNITS)
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Orden(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.CharField(max_length=100, unique=True)
    fecha = models.DateField()
    estado = models.BooleanField(blank=True, default=False)

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

