"""Modelos para la interfaz de administración de la 
aplicación de productos"""

#Django
from django.contrib import admin

#Models
from Productos.models import *

@admin.register(CaracteristicasDimensionale)
class CaracteristicasDimensionaleAdmin(admin.ModelAdmin):
    list_display = ('id_dimensiones','id_producto_c')
    search_fields = ('id_producto_c__Nombre_producto',)

@admin.register(PruebasEnsayo)
class PruebasEnsayoAdmin(admin.ModelAdmin):
    list_display = ('id_pruebas','id_producto_p')
    search_fields = ('id_producto_p__Nombre_producto',)

@admin.register(ControlAtributo)
class ControlAtributoAdmin(admin.ModelAdmin):
    list_display = ('id_atributo', 'id_producto_a')
    search_fields = ('id_producto_a__Nombre_producto',)


admin.site.register(Producto)
admin.site.register(NormasAplicable)
admin.site.register(Dimensiones)
admin.site.register(Pruebas)
admin.site.register(Atributos)
admin.site.register(Normas)
