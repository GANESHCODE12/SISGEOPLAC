"""Formularios de sistema documental"""

#Django
from django import forms

#Models
from Documentación.models import Documentacion


class DateInput(forms.DateInput):
    """Clase para mejorar el estilo del campo de fecha"""

    input_type = 'date'


class CrearDocumentoForm(forms.ModelForm):
    """Formulario para agregar documentos al listado maestro"""

    class Meta:
        model = Documentacion
        fields = '__all__'
        exclude = [
            'creado_por', 
            'actualizado_por'
        ]
        widgets = {
            'fecha': DateInput()
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


class ActualizarDocumentoForm(forms.ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = Documentacion
        fields = [
            'estado_documento',
            'control_cambios',
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