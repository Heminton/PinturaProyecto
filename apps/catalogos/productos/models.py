from django.db import models

from apps.catalogos.almacenes.models import Almacen
from apps.catalogos.catalogos.models import Catalogo
from apps.catalogos.marcas.models import Marca

"""
Producto
"""

class Producto(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    codigoColor = models.CharField(verbose_name='CodigoColor', max_length=100)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100, editable=False)
    precio = models.DecimalField(verbose_name='Precio', max_digits=7, decimal_places=2)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    marca = models.ForeignKey(Marca,verbose_name='Marca', on_delete=models.PROTECT)
    catalogo = models.ForeignKey(Catalogo,verbose_name='Catalogo', on_delete=models.PROTECT)
    almacen = models.ForeignKey(Almacen,verbose_name='Almacen', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.codigo} - {self.codigoColor} - {self.descripcion} - {self.precio} - {self.cantidad}"

    def save(self, *args, **kwargs):
        # Lógica para establecer el campo 'descripcion' según 'codigoColor'
        if self.codigoColor == '#217':
            self.descripcion = 'Dorado'
        elif self.codigoColor == '#214':
            self.descripcion = 'Marrón óxido'
        elif self.codigoColor == '#202':
            self.descripcion = 'Gris acero'
        else:
            self.descripcion = 'Descripción no definida'  # Valor por defecto si no coincide
        super(Producto, self).save(*args, **kwargs)

