from rest_framework.serializers import ModelSerializer, CharField
from .models import DetallePedido, Pedido

"""
    Serializador de la clase DetallePedido
"""
class DetallePedidoSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombre', read_only=True)
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad', 'producto_nombre']

"""
    Serializador de la clase Venta
"""
class VentaSerializer(ModelSerializer):
    cliente_nombre = CharField(source='cliente.nombres', read_only=True)
    #vendedor_nombre = CharField(source='vendedores.nombres', read_only=True)
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['cliente', 'cliente_nombre',  'detalles']


