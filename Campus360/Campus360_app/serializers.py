# Campus360_app/serializers.py

from rest_framework import serializers
from .models import Usuario, Libro, Boleta, Orden, Detalle_boleta, Carrito, ItemCarrito, DetalleOrden



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'isbn', 'titulo', 'autor', 'editorial', 'anio', 'genero', 'precio', 'imagen_url')

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_boleta
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

