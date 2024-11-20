from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Almacen
from .serializers import AlmacenSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from ...permissions import CustomPermission
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers
# from django.shortcuts import render
# from .forms import AlmacenFilter


# Configura el logger
logger = logging.getLogger(__name__)




class AlmacenApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los almacenes o crear un nuevo almacen.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Almacen  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: AlmacenSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los almacenes.
        """
        logger.info("GET request to list all almacenes")
        almacenes = Almacen.objects.all().order_by('id')
        page = self.paginate_queryset(almacenes,request)

        if page is not None:
            serializer = AlmacenSerializer(page, many=True)
            logger.info("Paginated response for almacenes")
            return self.get_paginated_response(serializer.data)

        serializer = AlmacenSerializer(almacenes, many=True)
        logger.error("Returning all almacenes without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AlmacenSerializer, responses={201: AlmacenSerializer})
    def post(self, request):
        """
        Crear un nuevo almacen.
        """
        logger.info("POST request to create a new almacen")

        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Almacen created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create almacen: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlmacenDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un almacen específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Almacen
    @swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un almacen por su ID.
        """

        logger.info("PUT request to update almacen with ID: %s", pk)

        almacen = get_object_or_404(Almacen, id=pk)
        if not almacen:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, almacen)  # Verificación de permisos
        serializer = AlmacenSerializer(almacen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Almacen updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update almacen with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un almacen por su ID.
        """
        logger.info("PATCH request to partially update almacen with ID: %s", pk)
        almacen = get_object_or_404(Almacen, id=pk)
        if not almacen:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, almacen)  # Verificación de permisos
        serializer = AlmacenSerializer(almacen, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Almacen partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update almacen with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un almacen por su ID.
        """
        logger.info("DELETE request to delete almacen with ID: %s", pk)
        almacen = get_object_or_404(Almacen, id=pk)
        if not almacen:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, almacen)  # Verificación de permisos
        almacen.delete()
        logger.info("Almacen deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
