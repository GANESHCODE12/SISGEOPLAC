"""Control production admin classes"""

#Django
from django.contrib import admin

#Models
import PNC.models

admin.site.register(PNC.models.ProductoNoConforme)
