from rest_framework.serializers import ModelSerializer

from apps.catalogos.marcas.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = ['codigo','descripcion']
        #fields = '__all__'