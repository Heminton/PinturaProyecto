from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Almacen
from .serializers import AlmacenSerializer
from drf_yasg.utils import swagger_auto_schema

class AlmacenApiView(APIView):
    """
    Vista para listar todos los Almacenes o crear un nuevo almacen.
    """
    @swagger_auto_schema(responses={200: AlmacenSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los departamentos.
        """
        almacenes = Almacen.objects.all()
        serializer = AlmacenSerializer(almacenes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AlmacenSerializer, responses={201: AlmacenSerializer})
    def post(self, request):
        """
        Crear un nuevo departamento.
        """
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AlmacenDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un Almacen en especifico.
    """

    @swagger_auto_schema(responses={200: AlmacenSerializer})
    def get(self, request, pk):
        """
        Obtener un Almacen especifico por su ID.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AlmacenSerializer(almacen)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un almacen por su ID.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return  Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlmacenSerializer(almacen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un almacen por su ID.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlmacenSerializer(almacen, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar un almacen por su ID.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return  Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        almacen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
