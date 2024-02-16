"""Control production admin classes"""

#Django
from django.contrib import admin

#Models
from Control_produccion.models import *


@admin.register(ControlProduccion)
class ControlProduccionAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero_op', 'hora_inicio', 'hora_final', 'tiempo_produccion']
    search_fields = ['id__exact', 'numero_op__numero_op__exact']

    def tiempo_produccion(self, obj):
        """Método para mostrar el tiempo total de producción"""
        return obj.tiempo_produccion

    tiempo_produccion.short_description = "Tiempo de Producción"

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
