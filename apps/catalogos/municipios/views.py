from rest_framework.viewsets import ModelViewSet
from .models import Municipio
from .serializers import MunicipioSerializer
from rest_framework.permissions import IsAuthenticated

class MunicipioViewSet(ModelViewSet):
    #perission_classes = [IsAuthenticated]
    queryset = Municipio.objects.all()  #Define el conjunto de datos
    serializer_class = MunicipioSerializer #Usa el serializador para los datos
