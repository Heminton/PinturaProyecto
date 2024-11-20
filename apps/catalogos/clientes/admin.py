from django.contrib import admin
from apps.catalogos.clientes.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['codigo','nombre','apellido','telefono','direccion']
    # ordering = ['codigo']  # ordena de manera ascedente los registros
