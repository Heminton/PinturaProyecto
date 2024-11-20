from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer
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




class ClienteApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los clientes o crear un nuevo cliente.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: ClienteSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los clientes.
        """
        logger.info("GET request to list all clientes")
        clientes = Cliente.objects.all().order_by('id')
        page = self.paginate_queryset(clientes,request)

        if page is not None:
            serializer = ClienteSerializer(page, many=True)
            logger.info("Paginated response for clientes")
            return self.get_paginated_response(serializer.data)

        serializer = ClienteSerializer(clientes, many=True)
        logger.error("Returning all clientes without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={201: ClienteSerializer})
    def post(self, request):
        """
        Crear un nuevo cliente.
        """
        logger.info("POST request to create a new cliente")

        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create cliente: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un cliente específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente
    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un cliente por su ID.
        """

        logger.info("PUT request to update cliente with ID: %s", pk)

        cliente = get_object_or_404(Cliente, id=pk)
        if not cliente:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente)  # Verificación de permisos
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update cliente with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un cliente por su ID.
        """
        logger.info("PATCH request to partially update cliente with ID: %s", pk)
        cliente = get_object_or_404(Cliente, id=pk)
        if not cliente:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente)  # Verificación de permisos
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update cliente with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un cliente por su ID.
        """
        logger.info("DELETE request to delete cliente with ID: %s", pk)
        cliente = get_object_or_404(Cliente, id=pk)
        if not cliente:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente)  # Verificación de permisos
        cliente.delete()
        logger.info("Cliente deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    