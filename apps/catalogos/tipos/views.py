
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tipo
from .serializers import TipoSerializer
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




class TipoApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los tipos de pintura o crear un nuevo tipo de pintura.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Tipo  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: TipoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los tipos de pintura.
        """
        logger.info("GET request to list all tipos de pintura")
        tipos = Tipo.objects.all().order_by('id')
        page = self.paginate_queryset(tipos,request)

        if page is not None:
            serializer = TipoSerializer(page, many=True)
            logger.info("Paginated response for tipos de pintura")
            return self.get_paginated_response(serializer.data)

        serializer = TipoSerializer(tipos, many=True)
        logger.error("Returning all tipos de pintura without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoSerializer, responses={201: TipoSerializer})
    def post(self, request):
        """
        Crear un nuevo tipo de pintura.
        """
        logger.info("POST request to create a new types of paint")

        serializer = TipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Types of paint created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create types of paint: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un tipo de pintura específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Tipo
    @swagger_auto_schema(request_body=TipoSerializer, responses={200: TipoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un tipo de pintura por su ID.
        """

        logger.info("PUT request to update types of paint with ID: %s", pk)

        tipo = get_object_or_404(Tipo, id=pk)
        if not tipo:
            return Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipo)  # Verificación de permisos
        serializer = TipoSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("types of paint updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update types of paint with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoSerializer, responses={200: TipoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un tipo de pintura por su ID.
        """
        logger.info("PATCH request to partially update types of paint with ID: %s", pk)
        tipo = get_object_or_404(Tipo, id=pk)
        if not tipo:
            return Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipo)  # Verificación de permisos
        serializer = TipoSerializer(tipo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Types of paint partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update types of paint with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un tipo de pintura por su ID.
        """
        logger.info("DELETE request to delete types of paint with ID: %s", pk)
        tipo = get_object_or_404(Tipo, id=pk)
        if not tipo:
            return Response({'error': 'Tipo de pintura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tipo)  # Verificación de permisos
        tipo.delete()
        logger.info("types of paint deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
