from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Proveedor
from .serializers import ProveedorSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from apps.permissions import CustomPermission
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)




class ProveedorApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los proveedores o crear un nuevo proveedor.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Proveedor  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: ProveedorSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los proveedores.
        """
        logger.info("GET request to list all proveedores")
        proveedores = Proveedor.objects.all().order_by('id')
        page = self.paginate_queryset(proveedores,request)

        if page is not None:
            serializer = ProveedorSerializer(page, many=True)
            logger.info("Paginated response for proveedores")
            return self.get_paginated_response(serializer.data)

        serializer = ProveedorSerializer(proveedores, many=True)
        logger.error("Returning all proveedores without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={201: ProveedorSerializer})
    def post(self, request):
        """
        Crear un nuevo proveedor.
        """
        logger.info("POST request to create a new proveedor")

        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Proveedor created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create proveedor: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un proveedor específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Proveedor
    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un proveedor por su ID.
        """

        logger.info("PUT request to update proveedor with ID: %s", pk)

        proveedor = get_object_or_404(Proveedor, id=pk)
        if not proveedor:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, proveedor)  # Verificación de permisos
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Proveedor updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update proveedor with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un proveedor por su ID.
        """
        logger.info("PATCH request to partially update proveedor with ID: %s", pk)
        proveedor = get_object_or_404(Proveedor, id=pk)
        if not proveedor:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, proveedor)  # Verificación de permisos
        serializer = ProveedorSerializer(proveedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Proveedor partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update proveedor with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un proveedor por su ID.
        """
        logger.info("DELETE request to delete proveedor with ID: %s", pk)
        proveedor = get_object_or_404(Proveedor, id=pk)
        if not proveedor:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, proveedor)  # Verificación de permisos
        proveedor.delete()
        logger.info("Proveedor deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
