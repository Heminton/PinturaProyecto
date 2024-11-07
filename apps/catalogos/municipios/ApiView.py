from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Municipio
from .serializers import MunicipioSerializer

class MunicipioApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un municipio específico (si se proporciona pk) o todos los municipios.
        """
        if pk:
            try:
                municipio = Municipio.objects.get(pk=pk)
            except Municipio.DoesNotExist:
                return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MunicipioSerializer(municipio)
            return Response(serializer.data)
        else:
            municipios = Municipio.objects.all()
            serializer = MunicipioSerializer(municipios, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo municipio.
        """
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un municipio existente completamente.
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

    def patch(self, request, pk=None):
        """
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

    def delete(self, request, pk=None):
        """
        Eliminar un municipio.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]