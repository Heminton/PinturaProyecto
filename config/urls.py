
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Configuración de Swagger con drf_yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Definición de rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas para documentación de API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Rutas de JWT para autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obtener un token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Endpoint para refrescar el token JWT

    # Otras rutas de la app
    path('catalogo/', include('apps.catalogos.urls')),

    path('seguridad/', include('apps.seguridad.urls')),

    path('movimientos/', include('apps.movimientos.urls')),

]


