from django.contrib import admin
from apps.catalogos.productos.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','codigoColor','nombre','precio','stock','marca_nombre','almacen_nombre','tipo_nombre']

    def marca_nombre(self, obj):
        return obj.marca.nombre

    marca_nombre.short_description = 'Marca'


    def almacen_nombre(self, obj):
        return obj.almacen.nombre

    almacen_nombre.short_description = 'Almacen'


    def tipo_nombre(self, obj):
        return obj.tipo.nombre

    tipo_nombre.short_description = 'Tipo'







