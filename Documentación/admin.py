"""Modelos para la interfaz de administración de la 
aplicación de documentación"""

#Django
from django.contrib import admin

#Models
from Documentación.models import Documentacion


admin.site.register(Documentacion)