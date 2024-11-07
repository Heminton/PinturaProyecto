#from django.contrib import admin

#from apps.catalogos.almacen.models import Almacen

#@admin.register(Almacen)
#class AlmacenAdmin(admin.ModelAdmin):
 #   search_fields = ['id','nombre']
  #  list_display = ['codigo','nombre','telefono','direccion','email','url','municipio']



from django.contrib import admin
from apps.catalogos.almacenes.models import Almacen

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre', 'telefono', 'direccion', 'email', 'url']





