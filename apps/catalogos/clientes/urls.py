from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet
from .ViewSet import *



router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
#router.register(r'departamentosS', DepartamentoViewSetES, basename='departamentoSSS')

urlpatterns = [
    path('', include(router.urls)),
    #path('<int:pk>/activarDepartamento/', DepartamentoActivarView.as_view(), name='activar-departamento'),
    #path("", DepartamentoApiView.as_view(), name="departamentos"),
]