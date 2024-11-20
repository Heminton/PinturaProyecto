
from django.urls import path
from .views import ProveedorApiView,ProveedorDetails

urlpatterns = [
    path('', ProveedorApiView.as_view()),  # Para listar o crear proveedores
    path('<int:pk>', ProveedorDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]