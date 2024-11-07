from django.contrib import admin
from apps.catalogos.estados.models import Estado

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion','orden']
    ordering = ['codigo']  # ordena de manera ascedente los registros