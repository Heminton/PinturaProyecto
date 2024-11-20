from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Municipio
from .serializers import MunicipioSerializer
from drf_yasg.utils import swagger_auto_schema

class MunicipioApiView(APIView):
    """
    Vista para listar todos los municipios o crear un nuevo municipio.
    """



    @swagger_auto_schema(responses={200: MunicipioSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los municipios.
        """
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)




    @swagger_auto_schema(request_body=MunicipioSerializer, responses={201: MunicipioSerializer})
    def post(self, request):
        """
        Crear un nuevo municipio.
        """
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MunicipioDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un municipio en especifico.
    """

    @swagger_auto_schema(responses={200: MunicipioSerializer})
    def get(self, request, pk):
        """
        Obtener un municipio especifico por su ID.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MunicipioSerializer(municipio)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un municipio por su ID.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return  Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un municipio por su ID.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar un municipio por su ID.
        """
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return  Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





