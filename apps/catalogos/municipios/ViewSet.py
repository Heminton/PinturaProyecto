from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Municipio
from .serializers import MunicipioSerializer


class MunicipioViewSetES(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    def list(self, request):
        """
        GET /municipios/
        Devuelve la lista de todos los municipios.
        """
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        GET /municipios/{id}/
        Devuelve un municipio específico por ID.
        """
        try:
            municipios = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MunicipioSerializer(municipios)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /municipios/
        Crea un nuevo municipio.
        """
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /municipios/{id}/
        Actualiza completamente un municipio existente.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /municipios/{id}/
        Actualización parcial de un municipio.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /municipios/{id}/
        Elimina un municipio existente.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartamentoViewSet
#
# router = DefaultRouter()
# router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
