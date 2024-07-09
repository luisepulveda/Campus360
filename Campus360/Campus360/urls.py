# Campus360/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Campus360_app import views  # Asegúrate de importar las vistas de tu aplicación

urlpatterns = [
    path('', views.index, name='home'),  # Ruta raíz para la vista 'index'
    path('index.html', views.index, name='index'), 
    path('Perfil.html', views.perfil, name='perfil'),
    path('Calculo_nota.html', views.calculo_nota, name='calculo_nota'),
    path('Biblioteca360.html', views.biblioteca360, name='biblioteca360'),
    path('Venta_libro.html', views.venta_libro, name='venta_libro'),
    path('book.html/', views.book_view, name='book_view'),
    path('Registro.html', views.registro, name='registro'),
    path('login.html', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('admin/', admin.site.urls),
    path('api/libros/', views.lista_libros, name='lista_libros'),  # Ruta para la vista lista_libros
    path('api/libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),  # Ruta para detalle de libro por ID
    path('api/buscar-libros/', views.buscar_libros, name='buscar_libros'),  # Ruta para buscar libros por criterios
     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
