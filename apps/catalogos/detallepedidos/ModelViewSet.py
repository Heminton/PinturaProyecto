from rest_framework.viewsets import ModelViewSet
from .models import DetallePedido
from .serializers import DetallePedidoSerializer

class DepartamentoViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Departamento.
    """
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
