"""Modelos para la interfaz de administración de la 
aplicación de producción"""

#Django
from django.contrib import admin

#Models
from Produccion.models import *


admin.site.register(Produccion)