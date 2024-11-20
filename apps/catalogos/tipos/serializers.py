from rest_framework.serializers import ModelSerializer

from apps.catalogos.tipos.models import Tipo

class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['codigo', 'nombre']
        #fields = '__all__'