"""Formularios de gestión humana"""

# Django
from django.forms import *

# Models
from Gestion_Humana.models import *


class DateInput(DateInput):
    """Campo especial de fecha"""

    input_type = 'date'


class NuevoColaboradorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = InformacionColaborador
        fields = '__all__'
        widgets = {
            'nombres': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'apellidos': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'fecha_nacimiento': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'tipo_documento': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
            }),
            'numero_documento': NumberInput(attrs={
                'class': 'form-control',
            }),
            'hijos': NumberInput(attrs={
                'class': 'form-control',
            }),
            'telefono_contacto': NumberInput(attrs={
                'class': 'form-control',
            }),
            'nombre_emergencia': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'parentezco': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'telefono_emergencia': NumberInput(attrs={
                'class': 'form-control',
            }),
            'jefe_inmediato': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'tipo_contrato': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
            }),
            'cargo': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'fecha_vinculacion': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'fecha_desvinculacion': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
        }

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class OtroSiForm(ModelForm):

    class Meta:
        model = OtroSi
        fields = '__all__'
        exclude = [
            'colaborador'
        ]


class ActualizarOtroSiForm(ModelForm):

    class Meta:
        model = OtroSi
        fields = '__all__'
        exclude = [
            'colaborador'
        ]

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ActualizarColaboradorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = InformacionColaborador
        fields = '__all__'
        widgets = {
            'nombres': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'apellidos': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'fecha_nacimiento': DateInput(format='%Y-%m-%d'),
            'tipo_documento': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
            }),
            'numero_documento': NumberInput(attrs={
                'class': 'form-control',
            }),
            'hijos': NumberInput(attrs={
                'class': 'form-control',
            }),
            'telefono_contacto': NumberInput(attrs={
                'class': 'form-control',
            }),
            'nombre_emergencia': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'parentezco': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'telefono_emergencia': NumberInput(attrs={
                'class': 'form-control',
            }),
            'jefe_inmediato': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'tipo_contrato': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
            }),
            'cargo': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'fecha_vinculacion': DateInput(format='%Y-%m-%d'),
            'fecha_desvinculacion': DateInput(format='%Y-%m-%d'),
        }

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProcesosDisciplinariosForm(ModelForm):
    class Meta:
        model = ProcesosDisciplinarios
        fields = '__all__'
        exclude = [
            'colaborador'
        ]


class ActualizarProcesosDisciplinariosForm(ModelForm):
    class Meta:
        model = ProcesosDisciplinarios
        fields = '__all__'
        exclude = [
            'colaborador'
        ]

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TecnicoForm(ModelForm):
    class Meta:
        model = TecnicosOperarios
        fields = '__all__'

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ReportGestionHumanaForm(forms.Form):
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))


class EntregaDotacionForm(ModelForm):

    class Meta:
        model = EntregaDotacion
        fields = '__all__'
        exclude = [
            'colaborador'
        ]
        widgets = {
            'fecha_entrega': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
        }


class CapacitacionForm(ModelForm):

    class Meta:
        model = Capacitacion
        fields = '__all__'
        exclude = [
            'colaborador'
        ]
        widgets = {
            'fecha_capacitacion': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
        }


class ExamenesMedicosForm(ModelForm):

    class Meta:
        model = ExamenesMedicos
        fields = '__all__'
        exclude = [
            'colaborador'
        ]
        widgets = {
            'fecha_examen': DateInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }),
        }


class ActualizarExamenForm(ModelForm):
    class Meta:
        model = ExamenesMedicos
        fields = '__all__'
        exclude = [
            'colaborador'
        ]

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ActualizarDotacionForm(ModelForm):
    class Meta:
        model = EntregaDotacion
        fields = '__all__'
        exclude = [
            'colaborador'
        ]

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ActualizarCapacitacionForm(ModelForm):
    class Meta:
        model = Capacitacion
        fields = '__all__'
        exclude = [
            'colaborador'
        ]

    def save(self, commit: True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CrearProgramacionForm(ModelForm):
    """Modelo de formulario para creación de control
    de las ordenes de producción"""

    class Meta:
        """Configuración del formulario"""

        model = Programacion
        fields = '__all__'
        exclude = [
            'cumplimiento',
            'motivo_incumplimiento',
        ]
        widgets = {
            'turno': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'fecha_programacion': DateInput(
                format=['%d/%m/%Y'],
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                    'id': 'fecha_programacion',
                    'data-target': '#fecha_programacion',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'maquina': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
        }


class ActualizarProgramacionForm(ModelForm):
    """Modelo de formulario para creación de control
    de las ordenes de producción"""

    class Meta:
        """Configuración del formulario"""

        model = Programacion
        fields = '__all__'
        widgets = {
            'turno': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'fecha_programacion': DateInput(
                format=['%d/%m/%Y'],
                attrs={
                    'autocomplete': 'off',
                    'class': "form-control datetimepicker-input",
                    'id': 'fecha_programacion',
                    'data-target': '#fecha_programacion',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'maquina': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'cumplimiento': CheckboxInput(attrs={
                'class': 'form-control',
            }),
            'motivo_incumplimiento': Textarea(attrs={
                'class': 'form-control',
            }),
        }
