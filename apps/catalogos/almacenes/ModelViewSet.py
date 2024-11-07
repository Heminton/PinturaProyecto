from rest_framework.viewsets import ModelViewSet
from .models import Almacen
from .serializers import AlmacenSerializer

class AlmacenViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Almacen.
    """
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
