from rest_framework.viewsets import ModelViewSet
from .models import Catalogo
from .serializers import CatalogoSerializer
from rest_framework.permissions import IsAuthenticated

class CatalogoViewSet(ModelViewSet):
    #perission_classes = [IsAuthenticated]
    queryset = Catalogo.objects.all()  #Define el conjunto de datos
    serializer_class = CatalogoSerializer #Usa el serializador para los datos
