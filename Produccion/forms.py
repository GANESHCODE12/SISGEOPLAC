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
            'producto',
            'aprobacion_orden',
            'aprobacion_materia_prima',
            'aprobacion_pigmento',
            'materia_prima_adicional',
            'pigmento_adicional',
            'fecha_inicio_produccion'
        ]


class ActuaizarOrden(forms.ModelForm):

    class Meta:
        """Configuración del formulario"""

        model = Produccion
        widgets = {
            'fecha_inicio_produccion': DateInput(format=('%Y-%m-%d')),
            'fecha_entrega': DateInput(format=('%Y-%m-%d')),
        }
        fields = [
            'cantidad_requerida',
            'maquina',
            'estado_op',
            'fecha_entrega',
            'fecha_inicio_produccion',
            'observaciones',
            'aprobacion_orden',
            'materia_prima_adicional',
            'aprobacion_materia_prima',
            'pigmento_adicional',
            'aprobacion_pigmento',
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


class CrearDesarrolloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """Configuración del formulario"""

        model = Desarrollo
        fields = '__all__'
        widgets = {
            'fecha_limite_entrega': DateInput(),
            'fecha_fabricacion': DateInput(),
        }
        exclude = [
            'desarrollo_creado_por',
            'fecha_creacion_desarrollo'
            'usuario_actualizo_desarrollo'
            'fecha_actualizacion_desarrollo',
            'maquina',
        ]


class HistoricalForm(forms.Form):
    producto = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'placeholder': 'Ingrese el nombre del producto!',
    }))
