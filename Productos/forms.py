"""Formularios de productos"""

#Django
from django.forms import *

#Models
from Productos.models import *



class DateInput(DateInput):
    """Campo especial de fecha"""

    input_type = 'date'


class CrearProductoForm(ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = Producto
        fields = '__all__'
        widgets = {
            'Nombre_producto': TextInput(attrs = {
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'numero_ficha': NumberInput(attrs = {
                'class': 'form-control',
            }),
            'codigo_producto': TextInput(attrs = {
                'class': 'form-control',
                'autocomplete': 'off',
            }),
            'proceso': TextInput(attrs = {
                'class': 'form-control',
            }),
            'cliente_especifico': TextInput(attrs = {
                'class': 'form-control',
            }),
            'tipo_producto': TextInput(attrs = {
                'class': 'form-control',
            }),
            'fecha_vigencia': DateInput(
                format='%Y-%m-%d',
                attrs = {
                'class': "form-control",
            }),
            'version': NumberInput(attrs = {
                'class': 'form-control',
            }),
            'cavidades': NumberInput(attrs = {
                'autocomplete': 'off',
                'class': 'form-control',
            }),
            'peso': NumberInput(attrs = {
                'autocomplete': 'off',
                'class': 'form-control',
            }),
            'fecha_plano': DateInput(
                format='%Y-%m-%d',
                attrs = {
                'class': "form-control",
            }),
            'estado_ficha': Select(attrs = {
                'class': 'form-control',
            }),
            'ciclo': NumberInput(attrs = {
                'autocomplete': 'off',
                'class': 'form-control',
            }),
            'descripción_especificaciones': TextInput(attrs = {
                'class': 'form-control',
            }),
            'material': TextInput(attrs = {
                'class': 'form-control',
            }),
            'olor': TextInput(attrs = {
                'class': 'form-control',
            }),
            'color': TextInput(attrs = {
                'class': 'form-control',
            }),
            'sabor': TextInput(attrs = {
                'class': 'form-control',
            }),
            'pigmento': TextInput(attrs = {
                'class': 'form-control',
            }),
            'tipo': TextInput(attrs = {
                'class': 'form-control',
            }),
            'unidad_empaque': NumberInput(attrs = {
                'class': 'form-control',
            }),
            'forma_empaque': TextInput(attrs = {
                'class': 'form-control',
            }),
            'caja': TextInput(attrs = {
                'class': 'form-control',
            }),
            'bolsa': TextInput(attrs = {
                'class': 'form-control',
            }),
            'plano': TextInput(attrs = {
                'class': 'form-control',
            }),
            'elaborado': TextInput(attrs = {
                'class': 'form-control',
            }),
            'revisado': TextInput(attrs = {
                'class': 'form-control',
            }),
            'aprobado': TextInput(attrs = {
                'class': 'form-control',
            }),
            'vida_util': Textarea(attrs = {
                'class': 'form-control',
            }),
            'notas': Textarea(attrs = {
                'class': 'form-control',
            }),
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


class DimensionesForm(ModelForm):
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


class PruebasForm(ModelForm):
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


class AtributosForm(ModelForm):
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


class NormasForm(ModelForm):
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


class ActualizarProductoForm(ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = Producto
        fields = [
            'diagrama'
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