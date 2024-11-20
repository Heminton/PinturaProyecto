from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Municipio
from .serializers import MunicipioSerializer
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




class MunicipioApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los municipios o crear un nuevo municipio.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Municipio  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: MunicipioSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los municipios.
        """
        logger.info("GET request to list all municipios")
        municipios = Municipio.objects.all().order_by('id')
        page = self.paginate_queryset(municipios,request)

        if page is not None:
            serializer = MunicipioSerializer(page, many=True)
            logger.info("Paginated response for municipios")
            return self.get_paginated_response(serializer.data)

        serializer = MunicipioSerializer(municipios, many=True)
        logger.error("Returning all municipios without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={201: MunicipioSerializer})
    def post(self, request):
        """
        Crear un nuevo municipio.
        """
        logger.info("POST request to create a new municipio")

        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Municipio created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create municipio: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MunicipioDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un municipio específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Municipio
    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un municipio por su ID.
        """

        logger.info("PUT request to update municipio with ID: %s", pk)

        municipio = get_object_or_404(Municipio, id=pk)
        if not municipio:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, municipio)  # Verificación de permisos
        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Municipio updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update municipio with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un municipio por su ID.
        """
        logger.info("PATCH request to partially update municipio with ID: %s", pk)
        municipio = get_object_or_404(Municipio, id=pk)
        if not municipio:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, municipio)  # Verificación de permisos
        serializer = MunicipioSerializer(municipio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Municipio partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update municipio with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un municipio por su ID.
        """
        logger.info("DELETE request to delete municipio with ID: %s", pk)
        municipio = get_object_or_404(Municipio, id=pk)
        if not municipio:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, municipio)  # Verificación de permisos
        municipio.delete()
        logger.info("Municipio deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
