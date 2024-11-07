from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(ModelViewSet):
    #perission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()  #Define el conjunto de datos
    serializer_class = ClienteSerializer #Usa el serializador para los datos