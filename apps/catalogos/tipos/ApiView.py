from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tipo
from .serializers import TipoSerializer
from drf_yasg.utils import swagger_auto_schema

class TipoApiView(APIView):
    """
    Vista para listar todos los tipos de pintura o crear un nuevo tipo de pintura.
    """



    @swagger_auto_schema(responses={200: TipoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los tipos de pintura.
        """
        tipos = Tipo.objects.all()
        serializer = TipoSerializer(tipos, many=True)
        return Response(serializer.data)




    @swagger_auto_schema(request_body=TipoSerializer, responses={201: TipoSerializer})
    def post(self, request):
        """
        Crear un nuevo tipo de pintura.
        """
        serializer = TipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TipoDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un tipo de pintura en especifico.
    """

    @swagger_auto_schema(responses={200: TipoSerializer})
    def get(self, request, pk):
        """
        Obtener un tipo de pintura especifico por su ID.
        """
        try:
            tipo = Tipo.objects.get(pk=pk)
        except Tipo.DoesNotExist:
            return Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoSerializer(tipo)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=TipoSerializer, responses={200: TipoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un tipo de pintura por su ID.
        """
        try:
            tipo = Tipo.objects.get(pk=pk)
        except Tipo.DoesNotExist:
            return  Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoSerializer, responses={200: TipoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un tipo de pintura por su ID.
        """
        try:
            tipo = Tipo.objects.get(pk=pk)
        except Tipo.DoesNotExist:
            return Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoSerializer(tipo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar un tipo de pintura por su ID.
        """
        try:
            tipo = Tipo.objects.get(pk=pk)
        except Tipo.DoesNotExist:
            return  Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







