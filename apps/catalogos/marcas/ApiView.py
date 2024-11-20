from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Marca
from .serializers import MarcaSerializer
from drf_yasg.utils import swagger_auto_schema

class MarcaApiView(APIView):
    """
    Vista para listar todas las marcas o crear una nueva marca.
    """



    @swagger_auto_schema(responses={200: MarcaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las marcas.
        """
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)




    @swagger_auto_schema(request_body=MarcaSerializer, responses={201: MarcaSerializer})
    def post(self, request):
        """
        Crear una nueva marca.
        """
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MarcaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una marca en especifico.
    """

    @swagger_auto_schema(responses={200: MarcaSerializer})
    def get(self, request, pk):
        """
        Obtener una marca especifica por su ID.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MarcaSerializer(marca)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una marca por su ID.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return  Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una marca por su ID.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(marca, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar una marca por su ID.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return  Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







