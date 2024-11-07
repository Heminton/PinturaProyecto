from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Cliente.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
