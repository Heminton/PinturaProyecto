from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Producto
from .serializers import ProductoSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductoApiView(APIView):
    """
    Vista para listar todos los productos o crear un nuevo producto.
    """



    @swagger_auto_schema(responses={200: ProductoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los productos.
        """
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)




    @swagger_auto_schema(request_body=ProductoSerializer, responses={201: ProductoSerializer})
    def post(self, request):
        """
        Crear un nuevo producto.
        """
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductoDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un producto en especifico.
    """

    @swagger_auto_schema(responses={200: ProductoSerializer})
    def get(self, request, pk):
        """
        Obtener un producto especifico por su ID.
        """
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(producto)
        return  Response(serializer.data)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un producto por su ID.
        """
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return  Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un producto por su ID.
        """
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No content'})
    def delete(self, request, pk):
        """
        Eliminar un producto por su ID.
        """
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return  Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







