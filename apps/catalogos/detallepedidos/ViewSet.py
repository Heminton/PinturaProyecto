from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DetallePedido
from .serializers import DetallePedidoSerializer


class DetallePedidoViewSetES(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    def list(self, request):
        """
        GET /detallePedidos/
        Devuelve la lista de todos los detallePedidos.
        """
        detallePedidos = DetallePedido.objects.all()
        serializer = DetallePedidoSerializer(detallePedidos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        GET /detallePedidos/{id}/
        Devuelve un detallePedido específico por ID.
        """
        try:
            detallePedido = DetallePedido.objects.get(pk=pk)
        except DetallePedido.DoesNotExist:
            return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetallePedidoSerializer(detallePedido)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /detallePedidos/
        Crea un nuevo detallePedido.
        """
        serializer = DetallePedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /detallePedidos/{id}/
        Actualiza completamente un detallePedido existente.
        """
        try:
            detallePedido = DetallePedido.objects.get(pk=pk)
        except DetallePedido.DoesNotExist:
            return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetallePedidoSerializer(detallePedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /detallePedidos/{id}/
        Actualización parcial de un detallePedido.
        """
        try:
            detallePedido = DetallePedido.objects.get(pk=pk)
        except DetallePedido.DoesNotExist:
            return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetallePedidoSerializer(detallePedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /detallePedidos/{id}/
        Elimina un detallePedido existente.
        """
        try:
            detallePedido = DetallePedido.objects.get(pk=pk)
        except DetallePedido.DoesNotExist:
            return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detallePedido.delete()
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
