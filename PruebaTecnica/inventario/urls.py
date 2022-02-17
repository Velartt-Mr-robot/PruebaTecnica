from django.urls import URLPattern, path
from . import views

#Cual solicitud se realiza y a que vista pertenece

urlpatterns = [
    path('', views.inicio, name="inicio" ),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos , name='productos'),
    path('productos', views.productos , name='productos'),
    path('productos/crear', views.crear , name='crear'),
    path('productos/editar', views.editar , name='editar'),
    path('eliminar/<int:id>', views.eliminar , name='eliminar'),   
    path('productos/editar/<int:id>', views.editar , name='editar'),   
]

