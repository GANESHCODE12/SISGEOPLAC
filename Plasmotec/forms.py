from django.forms import *

from Productos.models import *


class TestForm(Form):
    id_producto = ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=Select(
            attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }
        )
    )

    id_dimensiones = ModelChoiceField(
        queryset=CaracteristicasDimensionale.objects.none(),
        widget=Select(
            attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }
        )
    )

    # search = CharField(
    #     widget=TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ingrese una descripción'
    #     })
    # )
    #Sin select2

    search = ModelChoiceField(
        queryset=CaracteristicasDimensionale.objects.none(),
        widget=Select(
            attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }
        )
    )