from pyexpat import model
from django.db import models
from .choices import tipoSeccion, ubicacion, cargo

class Seccion(models.Model):
    nombre = models.CharField(max_length=100, choices=tipoSeccion  ,null=True, verbose_name='Nombre')
    ubicacion = models.CharField(max_length=100, choices=ubicacion  , null=True, verbose_name='Ubicación')
    descripcion = models.CharField(max_length=100, null=True, verbose_name='Descripción')

    def seccion(self):
        return "{}, {}".format(self.nombre, self.ubicacion)

    def __str_(self):
        return self.seccion()

class Responsable(models.Model):
    nombre = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, null=True, verbose_name='Apellidos')
    cargo = models.CharField(max_length=100, choices=cargo  , null=True, verbose_name='Cargo')

    def responsable(self):
        return "{}, {}, {}".format(self.nombre, self.apellidos, self.cargo)

    def __str__(self):
        return self.responsable()

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, null=True, verbose_name='Descripción')
    serial = models.FloatField(max_length=100, null=True, verbose_name='Serial')
    valor = models.FloatField(max_length=100, null=True, verbose_name='Valor')
    fecha = models.DateField(max_length=100, null=True, verbose_name='Fecha')
    estado = models.BooleanField(max_length=100, null=True, verbose_name='Estado')
    seccion = models.ForeignKey(Seccion, null=True, on_delete=models.DO_NOTHING )
    cargo = models.ForeignKey(Responsable, null=True, on_delete=models.DO_NOTHING )

    def __str__(self):
        fila='Nombre: ' + self.nombre + "  -   " + 'Descripción: ' + self.descripcion
        return fila


