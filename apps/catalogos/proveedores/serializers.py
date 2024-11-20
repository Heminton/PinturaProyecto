from rest_framework.serializers import ModelSerializer

from apps.catalogos.proveedores.models import Proveedor

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre', 'apellido']
        #fields = '__all__'