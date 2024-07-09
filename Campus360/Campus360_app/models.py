from django.db import models

# Create your models here.

#myapp/models.py

from django.db import models
from django.contrib.auth.models import User  # Importar User si es necesario
from django.urls import path, include  


class Usuario(models.Model):
    id_usuario = models.CharField(max_length=50, primary_key=True, null=False)
    tipo_usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)  # Considerar models.PasswordField()

    def __str__(self):
        return f"{self.id_usuario} {self.tipo_usuario} {self.nombre} {self.apellido}"

class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True, null=False)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.isbn} {self.titulo} {self.autor} {self.editorial} {self.anio} {self.genero}"

class Boleta(models.Model):
    id_boleta = models.CharField(max_length=50, primary_key=True, null=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='boletas')
    fecha = models.DateField()
    detalle = models.CharField(max_length=50)
    monto = models.IntegerField()

    def __str__(self):
        return f"Boleta {self.id_boleta} de {self.id_usuario}"

class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ordenes')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Orden de {self.usuario} - {self.fecha}"

class Detalle_boleta(models.Model):
    id_detalle_boleta = models.CharField(max_length=50, primary_key=True)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='detalles_boleta')
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='detalles_boleta')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.id_detalle_boleta}, {self.id_boleta}, {self.id_libro}, {self.cantidad}"

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Carrito de {self.usuario}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='items_carrito')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.libro.titulo} en el carrito de {self.carrito.usuario} (Cantidad: {self.cantidad})"

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='detalles_orden', on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='detalles_orden')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo} en la orden {self.orden}"
