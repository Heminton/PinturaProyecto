from django.db import models
from apps.catalogos.clientes.models import Cliente
#from apps.catalogos.vendedores.models import Vendedores
from apps.catalogos.productos.models import Producto
"""
Pedidos
"""
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    #vendedores = models.ForeignKey(Vendedores, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"{self.id}"
        # return f"{self.cliente} - {self.vendedores} - {self.fecha} - {self.total}"



"""
DetallePedidos
"""
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles' , on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = 'DetallePedidos'

    def __str__(self):
        return f"{self.cantidad} - {self.subtotal}"
        # return f"{self.venta} - {self.producto} - {self.cantidad} - {self.subtotal}"
