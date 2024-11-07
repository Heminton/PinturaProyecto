from django.urls import path, include
from .views import MarcaApiView

#app_name= "marcas"

urlpatterns = [
    path("", MarcaApiView.as_view(), name="marcas"),
]