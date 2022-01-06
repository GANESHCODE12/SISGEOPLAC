"""Modelos para la interfaz de administración de la 
aplicación de productos"""

#Django
from django.contrib import admin

#Models
from Productos.models import *


admin.site.register(Producto)
admin.site.register(CaracteristicasDimensionale)
admin.site.register(PruebasEnsayo)
admin.site.register(ControlAtributo)
admin.site.register(NormasAplicable)
admin.site.register(Dimensiones)
admin.site.register(Pruebas)
admin.site.register(Atributos)
admin.site.register(Normas)
