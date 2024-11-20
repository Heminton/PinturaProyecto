from rest_framework.serializers import ModelSerializer, CharField
from .models import DetallePedido, Pedido

"""
    Serializador de la clase DetallePedido
"""
class DetallePedidoSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombre', read_only=True)
    cliente_nombre = CharField(source='cliente.nombres', read_only=True)
    proveedor_nombre = CharField(source='proveedores.nombres', read_only=True)
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad', 'producto_nombre','cliente','cliente_nombre','proveedor','proveedor_nombre']

"""
    Serializador de la clase Pedido
"""
class PedidoSerializer(ModelSerializer):
    cliente_nombre = CharField(source='cliente.nombres', read_only=True)
    producto_nombre = CharField(source='productos.nombres', read_only=True)
    # proveedor_nombre = CharField(source='proveedores.nombres', read_only=True)
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['cliente','cliente_nombre','producto','producto_nombre','detalles']


