from django.contrib import admin
from apps.catalogos.tipos.models import Tipo

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','nombre']
    # ordering = ['codigo']  # ordena de manera ascedente los registros
