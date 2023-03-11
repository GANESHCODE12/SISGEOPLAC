"""Formularios de Control calidad"""

#Django
from django.forms import *

#Models
from Control_calidad.models import *


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
            'turno',
            'observaciones',
        ]
        widgets = {
            'fecha_despacho': DateInput(),
        }  


class CrearCertificadoForm(ModelForm):
    
    class Meta:
        """Configuración del formulario"""

        model = CertificadosCalidad
        fields = [
            'fecha_despacho',
            'cliente_despacho',
            'codigo_cliente',
            'cantidad_solicitada',
            'empaque_y_embalaje',
            'observaciones'
        ]
        widgets = {
            'fecha_despacho': DateInput()
        }


class CrearInspeccionMpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """Configuración del formulario"""

        model = MateriaPrimaInsumos
        fields = [
            'arte_cliente',
            'unidades_muestra',
            'proveedor',
            'arte_ingreso',
            'unidades_empaque',
            'revisado_por',
            'estado',
            'observaciones',
        ]


class ActualizarInspeccionMpForm(ModelForm):
    class Meta:
        model = MateriaPrimaInsumos
        fields = ['certificado_proveedor']

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


class HistoricalForm(forms.Form):
    producto = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'placeholder': 'Ingrese el nombre del producto!',
    }))
