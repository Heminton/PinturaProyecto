
from django.contrib import admin
from apps.catalogos.almacenes.models import Almacen

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre', 'telefono', 'direccion', 'email', 'url','latitud','longitud','municipio_nombre']

    def municipio_nombre(self, obj):
        return obj.municipio.nombre

    municipio_nombre.short_description = 'Municipio'








