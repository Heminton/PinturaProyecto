from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetallePedido
from .serializers import DetallePedidoSerializer

class DetallePedidoApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un detallePedido específico (si se proporciona pk) o todos los detallePedidos.
        """
        if pk:
            try:
                detallePedido = DetallePedido.objects.get(pk=pk)
            except DetallePedido.DoesNotExist:
                return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = DetallePedidoSerializer(detallePedido)
            return Response(serializer.data)
        else:
            detallePedidos = DetallePedido.objects.all()
            serializer = DetallePedidoSerializer(detallePedidos, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo detallePedido.
        """
        serializer = DetallePedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un detallePedido existente completamente.
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

    def patch(self, request, pk=None):
        """
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

    def delete(self, request, pk=None):
        """
        Eliminar un detallePedido.
        """
        try:
            detallePedido = DetallePedido.objects.get(pk=pk)
        except DetallePedido.DoesNotExist:
            return Response({'error': 'DetallePedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detallePedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]