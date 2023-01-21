#Django
from django import forms

#Models
from Inventario.models import *


class CrearElementoForm(forms.ModelForm):
  """Formulario para creación de elementos de inventario de materia prima"""

  class Meta:
    """Configuración del formulario"""

    model = Materia_Prima_Insumo
    fields = '__all__'
    exclude = [
      'material_creado_por',
      'fecha_creacion_material',
      'material_actualizado_por',
      'fecha_actualizacion_material'
    ]

  def save(self, commit:True):
    data = {}
    form = super()
    try:
      if form.is_valid():
        instance = form.save()
        data = instance.toJSON()
      else:
        data['error'] = form.errors
    except Exception  as e:
      data['error'] = str(e)
    return data


class ReportPTForm(forms.Form):
  date_range = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'autocomplete': 'off'
  }))


class ReportMpiForm(forms.Form):
  date_range = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'autocomplete': 'off'
  }))