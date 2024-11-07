from django.urls import path, include

urlpatterns = [
 path('pedidos/', include('apps.movimientos.pedidos.urls')),
]
