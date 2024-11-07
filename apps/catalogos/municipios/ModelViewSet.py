from rest_framework.viewsets import ModelViewSet
from .models import Municipio
from .serializers import MunicipioSerializer

class MunicipioViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Departamento.
    """
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
