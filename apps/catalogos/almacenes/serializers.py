from rest_framework.serializers import ModelSerializer

from apps.catalogos.almacenes.models import Almacen

class AlmacenSerializer(ModelSerializer):
    class Meta:
        model = Almacen
        fields = ['codigo', 'nombre', 'telefono', 'direccion', 'email', 'url','latitud','longitud']
        # fields = ['codigo', 'nombre', 'telefono', 'direccion', 'email', 'url','latitud','longitud','municipio_nombre']
        #fields = '__all__'