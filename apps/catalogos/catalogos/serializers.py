from rest_framework.serializers import ModelSerializer

from apps.catalogos.catalogos.models import Catalogo

class CatalogoSerializer(ModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['codigo','descripcion']
        #fields = '__all__'