
from django.urls import path
from .views import ClienteApiView,ClienteDetails

urlpatterns = [
    path('', ClienteApiView.as_view()),  # Para listar o crear clientes
    path('<int:pk>', ClienteDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]