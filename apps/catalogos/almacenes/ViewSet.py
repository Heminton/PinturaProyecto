from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Almacen
from .serializers import AlmacenSerializer
from drf_yasg.utils import swagger_auto_schema

class AlmacenViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar, crear, obtener, actualizar y eliminar almacenes.
    """
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer


    # @swagger_auto_schema(responses={200: AlmacenSerializer(many=True)})
    def list(self, request):
        """
        Listar todos los almacenes.
        """
        return super().list(request)

   # @swagger_auto_schema(request_body=AlmacenSerializer, responses={201: AlmacenSerializer})
    def create(self, request):
        """
        Crear un nuevo almacen.
        """
        return super().create(request)

    #@swagger_auto_schema(responses={200: AlmacenSerializer})
    def retrieve(self, request, pk=None):
        """
        Obtener un almacen específico por su ID.
        """
        return super().retrieve(request, pk)

    #@swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def update(self, request, pk=None):
        """
        Actualizar completamente un almacen por su ID.
        """
        return super().update(request, pk)

   # @swagger_auto_schema(request_body=AlmacenSerializer, responses={200: AlmacenSerializer})
    def partial_update(self, request, pk=None):
        """
        Actualizar parcialmente un almacen por su ID.
        """
        return super().partial_update(request, pk)

   # @swagger_auto_schema(responses={204: 'No Content'})
    def destroy(self, request, pk=None):
        """
        Eliminar un almacen por su ID.
        """
        return super().destroy(request, pk)

# from django.urls import path, include
#
# urlpatterns = [
#
#     path('departamentos/', include('apps.catalogos.departamentos.urls')),
#     path('municipios/', include('apps.catalogos.municipios.urls')),
# ]


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Almacen
from .serializers import AlmacenSerializer
from drf_yasg.utils import swagger_auto_schema

class AlmacenViewSet(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    @swagger_auto_schema(responses={200: AlmacenSerializer(many=True)})
    def list(self, request):
        """
        GET /almacenes/
        Devuelve la lista de todos los almacenes.
        """
        almacenes = Almacen.objects.all()
        serializer = AlmacenSerializer(almacenes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        GET /almacenes/{id}/
        Devuelve un almacen específico por ID.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AlmacenSerializer(almacen)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /almacenes/
        Crea un nuevo almacenes.
        """
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
        PUT /almacenes/{id}/
        Actualiza completamente un almacen existente.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlmacenSerializer(almacen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        """
        PATCH /almacenes/{id}/
        Actualización parcial de un almacen.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlmacenSerializer(almacen, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /almacenes/{id}/
        Elimina un almacen existente.
        """
        try:
            almacen = Almacen.objects.get(pk=pk)
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        almacen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartamentoViewSet
#
# router = DefaultRouter()
# router.register('', DepartamentoViewSet, basename='departamento')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

