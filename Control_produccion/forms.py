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
            'numero_op': Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%'
                }
            ),
            'hora_inicio': DateTimeInput(
                attrs={
                    
                    'class': "form-control datetimepicker-input",
                }
            ),
            'hora_final': DateTimeInput(
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                }
            ),
            'tiempo_paradas': TimeInput(
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                }
            ),
        }
        

