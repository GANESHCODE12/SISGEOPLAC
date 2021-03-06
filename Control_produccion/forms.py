"""Formularios de control producción"""

#Django
from django.forms import *

#Models
from Control_produccion.models import *


#Modelo Control producción
class CrearControlForm(ModelForm):
    """Modelo de formulario para creación de control
    de las ordenes de producción"""

    class Meta:
        """Configuración del formulario"""

        model = ControlProduccion
        fields = '__all__'
        exclude = [
            'numero_op',
            'supervisor',
            'supervisor_actualizo'
        ]
        widgets = {
            'tecnico': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'operario': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'turno': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'cantidad_producida': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'ciclo_turno': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'cavidades_operacion': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'hora_inicio': DateTimeInput(
                format = ['%d/%m/%Y %H:%M'],
                attrs = {
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                    'id': 'hora_inicio',
                    'data-target': '#hora_inicio',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'hora_final': DateTimeInput(
                format = ['%d/%m/%Y %H:%M'],
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                    'id': 'hora_final',
                    'data-target': '#hora_final',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'tiempo_paradas': TimeInput(
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control",
                    'id': 'tiempo_paradas',
                    'data-target': '#tiempo_paradas',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'observaciones': Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
        }
        

