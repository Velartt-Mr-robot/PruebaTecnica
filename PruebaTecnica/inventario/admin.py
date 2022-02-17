from django.contrib import admin
from .models import Producto, Responsable, Seccion
# Register your models here.

admin.site.register(Producto)
admin.site.register(Seccion)
admin.site.register(Responsable)