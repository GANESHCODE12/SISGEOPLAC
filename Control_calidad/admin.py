"""Quality control admin classes"""

#Django
from django.contrib import admin

#Models
from Control_calidad.models import *

admin.site.register(ControlCalidad)
admin.site.register(PruebasCalidad)
admin.site.register(InspeccionDimensional)
admin.site.register(InspeccionAtributos)