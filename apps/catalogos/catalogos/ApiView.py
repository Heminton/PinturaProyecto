from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Catalogo
from .serializers import CatalogoSerializer

class CatalogoApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un catalogo específico (si se proporciona pk) o todos los catalogos.
        """
        if pk:
            try:
                catalogo = Catalogo.objects.get(pk=pk)
            except Catalogo.DoesNotExist:
                return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CatalogoSerializer(catalogo)
            return Response(serializer.data)
        else:
            catalogos = Catalogo.objects.all()
            serializer = CatalogoSerializer(catalogos, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo catalogo.
        """
        serializer = CatalogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un catalogo existente completamente.
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

    def patch(self, request, pk=None):
        """
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

    def delete(self, request, pk=None):
        """
        Eliminar un catalogo.
        """
        try:
            catalogo = Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            return Response({'error': 'Catalogo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        catalogo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]