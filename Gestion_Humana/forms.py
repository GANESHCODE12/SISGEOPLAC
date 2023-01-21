"""Formularios de gestión humana"""

#Django
from django.forms import *

#Models
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
      'nombres': TextInput(attrs = {
        'class': 'form-control',
        'autocomplete': 'off',
    }),
    'apellidos': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'fecha_nacimiento': DateInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'tipo_documento': Select(attrs = {
      'class': 'form-control select2',
      'style': 'width: 100%',
    }),
    'numero_documento': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'hijos': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'telefono_contacto': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'nombre_emergencia': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'parentezco': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'telefono_emergencia': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'jefe_inmediato': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'tipo_contrato': Select(attrs = {
      'class': 'form-control select2',
      'style': 'width: 100%',
    }),
    'cargo': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'fecha_vinculacion': DateInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'fecha_desvinculacion': DateInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
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
    

class ActualizarColaboradorForm(ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  class Meta:
    model = InformacionColaborador
    fields = '__all__'
    widgets = {
      'nombres': TextInput(attrs = {
        'class': 'form-control',
        'autocomplete': 'off',
    }),
    'apellidos': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'fecha_nacimiento': DateInput(format='%Y-%m-%d'),
    'tipo_documento': Select(attrs = {
      'class': 'form-control select2',
      'style': 'width: 100%',
    }),
    'numero_documento': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'hijos': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'telefono_contacto': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'nombre_emergencia': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'parentezco': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'telefono_emergencia': NumberInput(attrs = {
      'class': 'form-control',
    }),
    'jefe_inmediato': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'tipo_contrato': Select(attrs = {
      'class': 'form-control select2',
      'style': 'width: 100%',
    }),
    'cargo': TextInput(attrs = {
      'class': 'form-control',
      'autocomplete': 'off',
    }),
    'fecha_vinculacion': DateInput(format='%Y-%m-%d'),
    'fecha_desvinculacion': DateInput(format='%Y-%m-%d'),
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


class TecnicoForm(ModelForm):

  class Meta:
    model = TecnicosOperarios
    fields = '__all__'

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


class ReportGestionHumanaForm(forms.Form):
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))