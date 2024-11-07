from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Marca
from .serializers import MarcaSerializer

#class DepartamentoApiView(APIView):
#    def get(self, request):
#        serializer = DepartamentoSerializer(Departamento.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    def post(self, request):
#        serializer = DepartamentoSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_201_CREATED, data=serializer.data)







"""------------------------------------------------------------------------------"""

class MarcaApiView(APIView):

    def get(self, request, pk=None):
        # Si se proporciona el pk, obtenemos una sola marca, de lo contrario, todas las marcas
        if pk:
            try:
                marca = Marca.objects.get(pk=pk)
            except Marca.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Marca no encontrada"})
            serialize = MarcaSerializer(marca)
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        else:
            marcas = Marca.objects.all()
            serialize = MarcaSerializer(marcas, many=True)
            return Response(status=status.HTTP_200_OK, data=serialize.data)

    def post(self, request):
        serialize = MarcaSerializer(data=request.data)
        # Validar los datos enviados en el request
        if serialize.is_valid(raise_exception=True):
            serialize.save()  # Guardar la nueva marca
            return Response(status=status.HTTP_201_CREATED, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def put(self, request, pk):
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Marca no encontrada"})

        # Actualizar los datos de la marca
        serialize = MarcaSerializer(marca, data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def patch(self, request, pk):
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Marca no encontrada"})

        # Actualización parcial, solo actualiza los campos proporcionados
        serialize = MarcaSerializer(marca, data=request.data, partial=True)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def delete(self, request, pk):
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Marca no encontrada"})

        marca.delete()  # Eliminar la marca
        return Response(status=status.HTTP_204_NO_CONTENT)
