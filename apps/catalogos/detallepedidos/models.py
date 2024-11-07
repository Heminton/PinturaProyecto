from django.db import models
#para convertir la cantidad en decimal
from decimal import Decimal
#importa ValidationError
from django.core.exceptions import ValidationError
from apps.catalogos.pedidos.models import Pedido
from apps.catalogos.productos.models import Producto
"""
DetallePedido
"""

class DetallePedido(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(verbose_name='Precio', max_digits=7, decimal_places=2)
    total = models.DecimalField(verbose_name='Total', max_digits=10, decimal_places=2, editable=False)
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'DetallePedidos'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.cantidad} - {self.precio} - {self.total}"



    #Validacion para que la cantidad y el precio sean valores positivos
    def clean(self):
        super().clean()  # Llama a clean del padre
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que cero.')
        if self.precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero')


    #Calculo automático del total basado en la cantidad y el precio
    def save(self, *args, **kwargs):
        self.total = Decimal(self.cantidad) * self.precio  # convertir cantidad a Decimal
        super().save(*args, **kwargs)
