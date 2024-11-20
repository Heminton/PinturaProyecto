from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Marca
from .serializers import MarcaSerializer
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




class MarcaApiView(PaginationMixin,APIView):
    """
    Vista para listar todas las marcas o crear una nueva marca.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Marca  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: MarcaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las marcas.
        """
        logger.info("GET request to list all marcas")
        marcas = Marca.objects.all().order_by('id')
        page = self.paginate_queryset(marcas,request)

        if page is not None:
            serializer = MarcaSerializer(page, many=True)
            logger.info("Paginated response for marcas")
            return self.get_paginated_response(serializer.data)

        serializer = MarcaSerializer(marcas, many=True)
        logger.error("Returning all marcas without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={201: MarcaSerializer})
    def post(self, request):
        """
        Crear una nueva marca.
        """
        logger.info("POST request to create a new marca")

        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Marca created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create marca: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una marca específica.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Marca
    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una marca por su ID.
        """

        logger.info("PUT request to update marca with ID: %s", pk)

        marca = get_object_or_404(Marca, id=pk)
        if not marca:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca)  # Verificación de permisos
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Marca updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update marca with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una marca por su ID.
        """
        logger.info("PATCH request to partially update marca with ID: %s", pk)
        marca = get_object_or_404(Marca, id=pk)
        if not marca:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca)  # Verificación de permisos
        serializer = MarcaSerializer(marca, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Marca partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update marca with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una marca por su ID.
        """
        logger.info("DELETE request to delete marca with ID: %s", pk)
        marca = get_object_or_404(Marca, id=pk)
        if not marca:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca)  # Verificación de permisos
        marca.delete()
        logger.info("Marca deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
