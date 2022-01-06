"""Formularios de producción"""

#Django
from django import forms

#Models
from Produccion.models import *


class DateInput(forms.DateInput):
    """Campo especial de fecha"""

    input_type = 'date'


class CrearForm(forms.ModelForm):
    """Modelo de formulario para creación de 
    ordenes"""

    class Meta:
        """Configuración del formulario"""

        model = Produccion
        fields = '__all__'
        widgets = {
            'fecha_entrega': DateInput(),
        }
        exclude = [
            'usuario',
            'usuario_actualizo',
            'producto'
        ]


class ActuaizarOrden(forms.ModelForm):

    class Meta:
        """Configuración del formulario"""

        model = Produccion
        fields = [
            'cantidad_requerida',
            'maquina',
            'estado_op',
            'fecha_entrega',
            'referencia_pigmento',
            'lote',
            'observaciones'
        ]
    
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