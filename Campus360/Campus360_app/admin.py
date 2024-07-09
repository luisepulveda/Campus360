
from django.contrib import admin
from .models import Usuario, Libro, Boleta, Orden, Detalle_boleta, Carrito, ItemCarrito, DetalleOrden

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Boleta)
admin.site.register(Orden)



admin.site.register(Detalle_boleta)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(DetalleOrden)






