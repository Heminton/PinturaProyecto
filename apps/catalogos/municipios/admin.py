
from django.contrib import admin
from apps.catalogos.municipios.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre', 'departamento_nombre']
    #ordering = ['codigo']  # ordena de manera ascedente los registros

    def departamento_nombre(self, obj):
        return obj.departamento.nombre

    departamento_nombre.short_description = 'Departamento'

