from django.db import models

from apps.catalogos.municipios.models import Municipio


"""
Almacenes
"""




class Almacen(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    telefono = models.CharField(verbose_name='Teléfono', max_length=15)
    direccion = models.CharField(verbose_name='Dirección', max_length=100)
    email = models.CharField(verbose_name='Email', max_length=100)
    url = models.CharField(verbose_name='URL', max_length=100)
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.PROTECT)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Latitud
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Longitud

    class Meta:
        verbose_name_plural = 'Almacenes'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f" {self.nombre} "

