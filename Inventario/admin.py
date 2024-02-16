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


class IngresoAdmin(admin.ModelAdmin):
  list_display = (
    'ingreso_materia_prima',
  )
  list_filter = ('ingreso_materia_prima__proveedor', 'ingreso_materia_prima__referencia')
  search_fields = ['ingreso_materia_prima__nombre']


class RequisicionMateriaPrimaAdmin(admin.ModelAdmin):
  list_display = (
    'material_solicitado',
    'control_id',
    'numero_orden'
  )
  list_filter = ['material_solicitado']
  search_fields = ['control_id__id']


admin.site.register(Inventario)
admin.site.register(Requisicion_PT)
admin.site.register(Materia_Prima_Insumo, MateriaPrimaInsumoAdmin)
admin.site.register(Requisicion, RequisicionMateriaPrimaAdmin)
admin.site.register(Entrada, IngresoAdmin)

