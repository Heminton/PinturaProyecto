from django.urls import path
from .views import AlmacenApiView,AlmacenDetails
# from . import views

urlpatterns = [
    path('', AlmacenApiView.as_view()),  # Para listar o crear almacenes
    path('<int:pk>', AlmacenDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
    # path('almacen/mapa/', views.almacen_map, name='almacen_map'),
]