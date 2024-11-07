from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Estado
from .serializers import EstadoSerializer

class EstadoApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un estado específico (si se proporciona pk) o todos los estados.
        """
        if pk:
            try:
                estado = Estado.objects.get(pk=pk)
            except Estado.DoesNotExist:
                return Response({'error': 'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = EstadoSerializer(estado)
            return Response(serializer.data)
        else:
            estados = Estado.objects.all()
            serializer = EstadoSerializer(estados, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo estado.
        """
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un estado existente completamente.
        """
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response({'error': 'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstadoSerializer(estado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial de un estado.
        """
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response({'error': 'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstadoSerializer(estado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar un estado.
        """
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response({'error': 'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        estado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]