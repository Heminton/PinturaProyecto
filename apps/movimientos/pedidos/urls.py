from django.urls import path
from .views import PedidoAPIView

app_name = 'pedido'


urlpatterns = [

    path('', PedidoAPIView.as_view(), name='pedidos'),
]