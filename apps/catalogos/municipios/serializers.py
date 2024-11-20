from rest_framework.serializers import ModelSerializer

from apps.catalogos.municipios.models import Municipio

class MunicipioSerializer(ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['codigo', 'nombre']
        # fields = ['codigo', 'nombre', 'departamento_nombre']
        #fields = '__all__'