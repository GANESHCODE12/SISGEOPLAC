"""Formularios de Control calidad"""

#Django
from django.forms import *

#Models
from Control_calidad.models import *

#Utilidades
from datetime import datetime

#Campos especiales
class DateInput(DateInput):
    """Se usa para dar formato especial en el template
    al campo hora"""

    input_type = 'date'


class CrearInspeccionForm(ModelForm):

    """Modelo para la creación de inspecciones"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """Configuración del formulario"""

        model = ControlCalidad
        fields = [
            'tecnico',
            'operario',
            'turno',
            'fecha_despacho',
            'cantidad_solicitada',
            'empaque_y_embalaje',
            'observaciones',
        ]
        widgets = {
            'fecha_despacho': DateInput(),
        }  


class ActualizarInspeccionForm(ModelForm):
    
    class Meta:
        """Configuración del formulario"""

        model = ControlCalidad
        fields = [
            'fecha_despacho',
            'cliente',
            'cantidad_solicitada',
            'empaque_y_embalaje',
            'observaciones',
        ]
        widgets = {
            'fecha_despacho': DateInput()
        }
    
    def save(self, commit:True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception  as e:
            data['error'] = str(e)
        return data