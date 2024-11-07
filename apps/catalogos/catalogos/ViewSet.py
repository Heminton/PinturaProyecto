from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Catalogo
from .serializers import CatalogoSerializer


class CatalogoViewSetES(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    def list(self, request):
        """
        GET /catalogos/
        Devuelve la lista de todos los catalogos.
        """
        catalogos = Catalogo.objects.all()
        serializer = CatalogoSerializer(catalogos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        GET /catalogos/{id}/
        Devuelve un catalogo específico por ID.
        """
        try:
            catalogo = Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            return Response({'error': 'Catalogo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CatalogoSerializer(catalogo)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /catalogos/
        Crea un nuevo catalogo.
        """
        serializer = CatalogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /catalogos/{id}/
        Actualiza completamente un catalogos existente.
        """
        try:
            catalogo = Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            return Response({'error': 'Catalogo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CatalogoSerializer(catalogo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /catalogos/{id}/
        Actualización parcial de un catalogo.
        """
        try:
            catalogo = Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            return Response({'error': 'Catalogo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CatalogoSerializer(catalogo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /catalogos/{id}/
        Elimina un catalogo existente.
        """
        try:
            catalogo = Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            return Response({'error': 'Catalogo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        catalogo.delete()
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
