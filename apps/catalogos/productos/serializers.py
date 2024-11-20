from rest_framework.serializers import ModelSerializer, CharField
from apps.catalogos.productos.models import Producto
"""
    Serializador de la clase Producto
"""

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo','codigoColor','nombre','precio','stock']
        #fields = '__all__'