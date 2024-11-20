
from django.urls import path
from .views import ProductoApiView,ProductoDetails

urlpatterns = [
    path('', ProductoApiView.as_view()),  # Para listar o crear departamentos
    path('<int:pk>', ProductoDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]