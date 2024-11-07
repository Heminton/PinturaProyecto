from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import VentaSerializer
from .models import Pedido,  DetallePedido, Producto, Cliente
from drf_yasg.utils import swagger_auto_schema

"""
    Enpoint de Venta
"""

class PedidoAPIView(APIView):
    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    cliente = get_object_or_404(Cliente, id=serializer.validated_data.get('cliente').id)
                    # vendedor = get_object_or_404(Vendedores, id=serializer.validated_data.get('vendedores').id)
                    detalles_data = serializer.validated_data.get('detalles')
                    pedido = Pedido.objects.create(cliente=cliente, total=0)
                    total_venta= 0;

                    for detalles_data in detalles_data:
                        cantidad = detalles_data['cantidad']
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)

                        if producto.stock < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombre}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                        subtotal = producto.precio * cantidad
                        total_venta += subtotal

                        producto.stock -= cantidad
                        producto.save()

                        DetallePedido.objects.create(
                            pedido=pedido,
                            producto=producto,
                            cantidad=cantidad,
                            subtotal=subtotal
                        )
                    pedido.total = total_venta
                    pedido.save()

                    venta_serializer = VentaSerializer(pedido)
                    return Response(venta_serializer.data, status=status.HTTP_201_CREATED)



            except Exception as e:
                Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)