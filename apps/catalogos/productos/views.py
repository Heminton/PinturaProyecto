from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from ...permissions import CustomPermission
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)




class ProductoApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los productos o crear un nuevo producto.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: ProductoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los productos.
        """
        logger.info("GET request to list all productos")
        productos = Producto.objects.all().order_by('id')
        page = self.paginate_queryset(productos,request)

        if page is not None:
            serializer = ProductoSerializer(page, many=True)
            logger.info("Paginated response for productos")
            return self.get_paginated_response(serializer.data)

        serializer = ProductoSerializer(productos, many=True)
        logger.error("Returning all productos without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={201: ProductoSerializer})
    def post(self, request):
        """
        Crear un nuevo producto.
        """
        logger.info("POST request to create a new producto")

        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Producto created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create producto: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un producto específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto
    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un producto por su ID.
        """

        logger.info("PUT request to update producto with ID: %s", pk)

        producto = get_object_or_404(Producto, id=pk)
        if not producto:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, producto)  # Verificación de permisos
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Producto updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update producto with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un producto por su ID.
        """
        logger.info("PATCH request to partially update producto with ID: %s", pk)
        producto = get_object_or_404(Producto, id=pk)
        if not producto:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, producto)  # Verificación de permisos
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Producto partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update producto with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un producto por su ID.
        """
        logger.info("DELETE request to delete producto with ID: %s", pk)
        producto = get_object_or_404(Producto, id=pk)
        if not producto:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, producto)  # Verificación de permisos
        producto.delete()
        logger.info("Producto deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
