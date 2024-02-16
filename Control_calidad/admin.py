"""Quality control admin classes"""

#Django
from django.contrib import admin

#Models
from Control_calidad.models import *
from Produccion.models import *


@admin.register(ControlCalidad)
class ControlCalidadAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'numero_op',
    'get_producto',
  )
  list_filter = ('numero_op__producto', )
  search_fields = ['id__exact']
  

  def get_producto(self, obj):
    production_object = Produccion.objects.get(numero_op=obj.numero_op_id)
    return str(production_object.producto)


@admin.register(PruebasCalidad)
class PruebasCalidadAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'inspeccion',
    'pruebas_y_o_ensayos',
    'get_producto',
  )
  list_filter = ('id_inspeccion_p__numero_op__producto', )
  search_fields = ['id_inspeccion_p__exact']

  def inspeccion(self, obj):
        return obj.id_inspeccion_p_id

  def get_producto(self, obj):
    production_object = Produccion.objects.get(numero_op=obj.id_inspeccion_p.numero_op_id)
    return str(production_object.producto)


@admin.register(InspeccionDimensional)
class InspeccionDimensionalAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'inspeccion',
    'get_dimension',
    'get_producto',
  )
  list_filter = ('id_inspeccion_d__numero_op__producto', )
  search_fields = ['id_inspeccion_d__exact']

  def inspeccion(self, obj):
        return obj.id_inspeccion_d_id

  def get_producto(self, obj):
    production_object = Produccion.objects.get(numero_op=obj.id_inspeccion_d.numero_op_id)
    return str(production_object.producto)

  def get_dimension(self, obj):
    return obj.inspeccion_dimensional.id_dimensiones


@admin.register(InspeccionAtributos)
class InspeccionAtributosAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'inspeccion',
    'inspeccion_atributos',
    'get_producto',
  )
  list_filter = ('id_inspeccion_a__numero_op__producto', )
  search_fields = ['id_inspeccion_a__exact']

  def inspeccion(self, obj):
    return obj.id_inspeccion_a_id

  def get_producto(self, obj):
    production_object = Produccion.objects.get(numero_op=obj.id_inspeccion_a.numero_op_id)
    return str(production_object.producto)


@admin.register(ColaboradorInspeccionCalidad)
class ColaboradorInspeccionCalidadAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'get_inspeccion',
    'colaborador',
  )
  list_filter = ('inspeccion__numero_op__producto', )
  search_fields = ['inspeccion__exact']

  def get_inspeccion(self, obj):
    return obj.inspeccion_id


@admin.register(CertificadosCalidad)
class CertificadosCalidadAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'get_inspeccion',
  )
  list_filter = ('inspeccion_certificado__numero_op__producto', )
  search_fields = ['inspeccion_certificado__exact']

  def get_inspeccion(self, obj):
    return obj.inspeccion_certificado_id


@admin.register(NivelDeInspeccion)
class NivelDeInspeccionAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'get_inspeccion',
    'tipo_nivel',
    'codigo_nivel'
  )
  list_filter = ('inspeccion_calidad__numero_op__producto', )
  search_fields = ['inspeccion_calidad__exact']

  def get_inspeccion(self, obj):
    return obj.inspeccion_calidad_id