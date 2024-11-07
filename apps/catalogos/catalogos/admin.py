from django.contrib import admin
from apps.catalogos.catalogos.models import Catalogo

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','descripcion']
    ordering = ['codigo']  # ordena de manera ascedente los registros
