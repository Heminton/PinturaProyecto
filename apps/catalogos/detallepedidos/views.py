from rest_framework.viewsets import ModelViewSet
from .models import DetallePedido
from .serializers import DetallePedidoSerializer
from rest_framework.permissions import IsAuthenticated

class DetallePedidoViewSet(ModelViewSet):
    #perission_classes = [IsAuthenticated]
    queryset = DetallePedido.objects.all()  #Define el conjunto de datos
    serializer_class = DetallePedidoSerializer #Usa el serializador para los datos
