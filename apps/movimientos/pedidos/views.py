from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import PedidoSerializer
from .serializers import DetallePedidoSerializer
from .models import Pedido,  DetallePedido, Producto, Cliente, Proveedor
from drf_yasg.utils import swagger_auto_schema

"""
    Enpoint de Pedido
"""

class PedidoAPIView(APIView):
    @swagger_auto_schema(request_body=PedidoSerializer)
    def post(self, request):
        serializer = PedidoSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    cliente = get_object_or_404(Cliente, id=serializer.validated_data.get('cliente').id)
                    proveedor = get_object_or_404(Proveedor, id=serializer.validated_data.get('proveedores').id)
                    detalles_data = serializer.validated_data.get('detalles')
                    pedido = Pedido.objects.create(cliente=cliente, proveedores= proveedor, total=0)
                    total_pedido= 0;

                    for detalle_data in detalles_data:
                        cantidad = detalle_data['cantidad']
                        producto = get_object_or_404(Producto, id=detalle_data['producto'].id)

                        if producto.stock < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombre}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                        subtotal = producto.precio * cantidad
                        total_pedido += subtotal

                        producto.stock -= cantidad
                        producto.save()

                        DetallePedido.objects.create(
                            pedido=pedido,
                            producto=producto,
                            cantidad=cantidad,
                            subtotal=subtotal
                        )
                    pedido.total = total_pedido
                    pedido.save()

                    pedido_serializer = PedidoSerializer(pedido)
                    return Response(pedido_serializer.data, status=status.HTTP_201_CREATED)



            except Exception as e:
                Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










