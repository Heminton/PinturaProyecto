from django.urls import path
from .views import AlmacenApiView,AlmacenDetails

urlpatterns = [
    path('', AlmacenApiView.as_view()),  # Para listar o crear departamentos
    path('<int:pk>', AlmacenDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]