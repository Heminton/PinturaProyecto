from django.urls import path, include
from .views import EstadoApiView

#app_name= "estados"

urlpatterns = [
    path("", EstadoApiView.as_view(), name="estados"),
]