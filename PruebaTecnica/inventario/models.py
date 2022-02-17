from pyexpat import model
from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, null=True, verbose_name='Descripción')
    serial = models.FloatField(max_length=100, null=True, verbose_name='Serial')
    valor = models.FloatField(max_length=100, null=True, verbose_name='Valor')
    fecha = models.DateField(max_length=100, null=True, verbose_name='Fecha')
    estado = models.BooleanField(max_length=100, null=True, verbose_name='Estado')

    def __str__(self):
        fila='Nombre: ' + self.nombre + "  -   " + 'Descripción: ' + self.descripcion
        return fila
