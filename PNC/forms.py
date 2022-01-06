"""Formularios de Producto no conforme"""

#Django
from django import forms

#Models
from PNC.models import ProductoNoConforme


#Campos especiales
class DateInput(forms.DateInput):
    """Se usa para dar formato especial en el template
    al campo hora"""

    input_type = 'date'


#Modelo Control producción
class CrearPncForm(forms.ModelForm):
    """Modelo de formulario para creación de PNC
    de las ordenes de producción"""

    class Meta:
        """Configuración del formulario"""

        model = ProductoNoConforme
        fields = '__all__'
        widgets = {
            'fecha_pnc': DateInput()
        }
        exclude = [
            'inspector_calidad',
            'inspector_calidad_actualiza',
            'id_inspeccion',
        ]


class ActualizarPNC(forms.ModelForm):

    class Meta:
        """Configuración del formulario"""

        model = ProductoNoConforme
        fields = [
            'estado_pnc',    
            'cantidad_pnc',
            'observaciones',
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