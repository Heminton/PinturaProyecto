
from django.urls import path
from .views import TipoApiView,TipoDetails

urlpatterns = [
    path('', TipoApiView.as_view()),  # Para listar o crear tipos de pintura
    path('<int:pk>', TipoDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]