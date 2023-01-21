from django.contrib import admin

# Register your models here.

#Django
from django.contrib import admin

#Models
from Inventario.models import *

admin.site.register(Inventario)
admin.site.register(Requisicion_PT)
admin.site.register(Materia_Prima_Insumo)
admin.site.register(Requisicion)
admin.site.register(Entrada)
