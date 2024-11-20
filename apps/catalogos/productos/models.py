from django.db import models

from apps.catalogos.marcas.models import Marca
from apps.catalogos.almacenes.models import Almacen
from  apps.catalogos.tipos.models import Tipo

"""
Producto
"""

class Producto(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    codigoColor = models.CharField(verbose_name='CodigoColor', max_length=100)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    precio = models.DecimalField(verbose_name='Precio', max_digits=7, decimal_places=2)
    stock = models.IntegerField(verbose_name='Stock')
    marca = models.ForeignKey(Marca,verbose_name='Marca', on_delete=models.PROTECT)
    almacen = models.ForeignKey(Almacen,verbose_name='Almacen', on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, verbose_name='Tipo', on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = 'Productos'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.nombre}"
        # return f"{self.codigo} - {self.codigoColor} - {self.descripcion} - {self.precio} - {self.cantidad}"



