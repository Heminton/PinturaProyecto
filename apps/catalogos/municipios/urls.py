
from django.urls import path
from .views import MunicipioApiView,MunicipioDetails

urlpatterns = [
    path('', MunicipioApiView.as_view()),  # Para listar o crear municipios
    path('<int:pk>', MunicipioDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]