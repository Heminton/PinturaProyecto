from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSetES(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    def list(self, request):
        """
        GET /clientes/
        Devuelve la lista de todos los clientes.
        """
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        GET /clientes/{id}/
        Devuelve un cliente específico por ID.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /clientes/
        Crea un nuevo cliente.
        """
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /clientes/{id}/
        Actualiza completamente un cliente existente.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /clientes/{id}/
        Actualización parcial de un cliente.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /clientes/{id}/
        Elimina un cliente existente.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        cliente.delete()
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
