from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Proveedor
from .serializers import ProveedorSerializer
from drf_yasg.utils import swagger_auto_schema

class ProveedorApiView(APIView):
    """
    Vista para listar todos los proveedores o crear un nuevo proveedor.
    """



    @swagger_auto_schema(responses={200: ProveedorSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los proveedores.
        """
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)




    @swagger_auto_schema(request_body=ProveedorSerializer, responses={201: ProveedorSerializer})
    def post(self, request):
        """
        Crear un nuevo proveedor.
        """
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProveedorDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un proveedor en especifico.
    """

    @swagger_auto_schema(responses={200: ProveedorSerializer})
    def get(self, request, pk):
        """
        Obtener un proveedor especifico por su ID.
        """
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProveedorSerializer(proveedor)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un proveedor por su ID.
        """
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return  Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un proveedor por su ID.
        """
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProveedorSerializer(proveedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar un proveedor por su ID.
        """
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return  Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







