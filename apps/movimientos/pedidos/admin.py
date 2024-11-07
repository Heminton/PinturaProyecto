from django.contrib import admin
from apps.movimientos.pedidos.models import Pedido
from apps.movimientos.pedidos.models import DetallePedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ['id', "cliente"]
    list_display = ['cliente','fecha', 'total']


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    search_fields = ['id', "pedido"]
    list_display = ['pedido','producto','cantidad', 'subtotal']
