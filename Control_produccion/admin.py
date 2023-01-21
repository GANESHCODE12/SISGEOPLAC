"""Control production admin classes"""

#Django
from django.contrib import admin

#Models
from Control_produccion.models import *


admin.site.register(ControlProduccion)

@admin.register(ColaboradorControlProduccion)
class ColaboradorControlProduccionAdmin(admin.ModelAdmin):
  list_display = (
    'control',
    'colaborador',
  )
  search_fields = ['control__id__exact']

@admin.register(TiemposParadasControlProduccion)
class TiemposParadasControlProduccionAdmin(admin.ModelAdmin):
  list_display = (
    'control',
    'motivo',
  )
  search_fields = ['control__id__exact']
