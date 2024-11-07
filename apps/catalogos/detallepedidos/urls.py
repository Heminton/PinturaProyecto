from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DetallePedidoViewSet
from .ViewSet import *



router = DefaultRouter()
router.register(r'detallePedidos', DetallePedidoViewSet, basename='detallePedidos')
#router.register(r'detallePedidosS', DepartamentoViewSetES, basename='departamentoSSS')

urlpatterns = [
    path('', include(router.urls)),
    #path('<int:pk>/activarDepartamento/', DepartamentoActivarView.as_view(), name='activar-departamento'),
    #path("", DepartamentoApiView.as_view(), name="departamentos"),
]