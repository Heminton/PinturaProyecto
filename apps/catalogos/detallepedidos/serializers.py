from rest_framework.serializers import ModelSerializer

from apps.catalogos.detallepedidos.models import DetallePedido

class DetallePedidoSerializer(ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['codigo','descripcion','cantidad','precio','total']
        #fields = '__all__'