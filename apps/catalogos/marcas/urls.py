
from django.urls import path
from .views import MarcaApiView,MarcaDetails

urlpatterns = [
    path('', MarcaApiView.as_view()),  # Para listar o crear marcas
    path('<int:pk>', MarcaDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]