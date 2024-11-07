from rest_framework.viewsets import ModelViewSet
from .models import Catalogo
from .serializers import CatalogoSerializer

class CatalogoViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Catalogo.
    """
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer
