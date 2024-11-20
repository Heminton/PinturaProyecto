
from django.urls import path
from .views import DepartamentoApiView,DepartamentoDetails

urlpatterns = [
    path('', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
    path('<int:pk>', DepartamentoDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]