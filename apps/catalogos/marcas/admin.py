from django.contrib import admin
from apps.catalogos.marcas.models import Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','descripcion']
    ordering = ['codigo']  # ordena de manera ascedente los registros


