from django.contrib import admin
from django.contrib import admin
from apps.catalogos.proveedores.models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['codigo','nombre','apellido']
