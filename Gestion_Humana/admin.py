#Django
from django.contrib import admin

#Models
from Gestion_Humana.models import *


@admin.register(TecnicosOperarios)
class TecnicosOperariosAdmin(admin.ModelAdmin):
  list_display = (
    'nombre',
    'cargo',
    'codigo',
  )
  search_fields = ['nombre__icontains']
  