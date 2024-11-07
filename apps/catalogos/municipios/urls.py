from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MunicipioViewSet
from .ViewSet import *



router = DefaultRouter()
router.register(r'municipios', MunicipioViewSet, basename='municipio')
#router.register(r'municipiosS', MunicipioViewSetES, basename='municipioSSS')

urlpatterns = [
    path('', include(router.urls)),
    #path('<int:pk>/activarMunicipio/', MunicipioActivarView.as_view(), name='activar-municipio'),
    #path("", MunicipioApiView.as_view(), name="municipios"),
]