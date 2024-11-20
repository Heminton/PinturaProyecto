from rest_framework.serializers import ModelSerializer

from apps.catalogos.clientes.models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre','apellido','telefono','direccion']
        #fields = '__all__'