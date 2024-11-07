from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Estado
from .serializers import EstadoSerializer

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

class EstadoApiView(APIView):

    def get(self, request, pk=None):
        # Si se proporciona el pk, obtenemos un solo estado, de lo contrario, todos los estados
        if pk:
            try:
                estado = Estado.objects.get(pk=pk)
            except Estado.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Estado no encontrado"})
            serialize = EstadoSerializer(estado)
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        else:
            estados = Estado.objects.all()
            serialize = EstadoSerializer(estados, many=True)
            return Response(status=status.HTTP_200_OK, data=serialize.data)

    def post(self, request):
        serialize = EstadoSerializer(data=request.data)
        # Validar los datos enviados en el request
        if serialize.is_valid(raise_exception=True):
            serialize.save()  # Guardar el nuevo estado
            return Response(status=status.HTTP_201_CREATED, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def put(self, request, pk):
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Estado no encontrado"})

        # Actualizar los datos del estado
        serialize = EstadoSerializer(estado, data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def patch(self, request, pk):
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Estado no encontrado"})

        # Actualización parcial, solo actualiza los campos proporcionados
        serialize = EstadoSerializer(estado, data=request.data, partial=True)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(status=status.HTTP_200_OK, data=serialize.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)

    def delete(self, request, pk):
        try:
            estado = Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Estado no encontrado"})

        estado.delete()  # Eliminar el estado
        return Response(status=status.HTTP_204_NO_CONTENT)