from django.urls import path, include

urlpatterns = [
 path('departamentos/', include('apps.catalogos.departamentos.urls')),

 path('municipios/', include('apps.catalogos.municipios.urls')),

 path('almacenes/', include('apps.catalogos.almacenes.urls')),

 path('catalogos/', include('apps.catalogos.catalogos.urls')),

 path('clientes/', include('apps.catalogos.clientes.urls')),

 #path('estados/', include('apps.catalogos.estados.urls')),

 #path('marcas/', include('apps.catalogos.marcas.urls')),
]