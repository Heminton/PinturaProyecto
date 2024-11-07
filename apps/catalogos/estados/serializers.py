from rest_framework.serializers import ModelSerializer

from apps.catalogos.estados.models import Estado

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = ['codigo','descripcion','orden']
        #fields = '__all__'