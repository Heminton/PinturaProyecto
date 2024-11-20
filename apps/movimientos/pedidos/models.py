from django.db import models
from apps.catalogos.clientes.models import Cliente
from apps.catalogos.productos.models import Producto
from apps.catalogos.proveedores.models import Proveedor

"""
Pedidos
"""
class Pedido(models.Model):
    # Definir las opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('PROCESANDO', 'Procesando'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PROCESANDO', verbose_name='Estado')
    orden = models.IntegerField(verbose_name='Orden', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        verbose_name_plural = 'Pedidos'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        # Asignar el campo 'orden' según el estado seleccionado
        estado_orden_map = {
            'PROCESANDO': 1,
            'COMPLETADO': 2,
            'CANCELADO': 3,
        }
        self.orden = estado_orden_map.get(self.estado, None)
        super(Pedido, self).save(*args, **kwargs)


"""
DetallePedidos
"""
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles' , on_delete=models.PROTECT) #id autoincremental de cada pedido
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        verbose_name_plural = 'DetallePedidos'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.cantidad} - {self.subtotal}"
        # return f"{self.venta} - {self.producto} - {self.cantidad} - {self.subtotal}"








