from django.contrib import admin

# Register your models here.

#Django
from django.contrib import admin

#Models
from Inventario.models import *

class MateriaPrimaInsumoAdmin(admin.ModelAdmin):
  list_display = (
    'nombre',
    'categoria',
    'referencia',
    'proveedor'
  )
  list_filter = ('nombre', 'referencia')
  search_fields = ['nombre']

admin.site.register(Inventario)
admin.site.register(Requisicion_PT)
admin.site.register(Materia_Prima_Insumo, MateriaPrimaInsumoAdmin)
admin.site.register(Requisicion)
admin.site.register(Entrada)
