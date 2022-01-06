"""Formularios de productos"""

#Django
from django import forms

#Models
from Productos.models import *



class DateInput(forms.DateInput):
    """Campo especial de fecha"""

    input_type = 'date'


class CrearProductoForm(forms.ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_vigencia': DateInput(),
            'fecha_plano': DateInput(),
        }
        exclude = [
            'elaborado_por', 
            'modificado_por'
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


class DimensionesForm(forms.ModelForm):
    """Modelo de formulario para creación de caracteristicas 
    dimensionales de la ficha técnica"""

    class Meta:
        """Configuración del formulario"""

        model = Dimensiones
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


class PruebasForm(forms.ModelForm):
    """Modelo de formulario para creación de pruebas de la
    ficha técnica"""

    class Meta:
        """Configuración del formulario"""

        model = Pruebas
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


class AtributosForm(forms.ModelForm):
    """Modelo de formulario para creación de control de
    atributos de la ficha técnica"""

    class Meta:
        """Configuración del formulario"""

        model = Atributos
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


class NormasForm(forms.ModelForm):
    """Modelo de formulario para creación de control de
    atributos de la ficha técnica"""

    class Meta:
        """Configuración del formulario"""

        model = Normas
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


class ActualizarProductoForm(forms.ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = Producto
        fields = [
            'estado_ficha',
            'notas'
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