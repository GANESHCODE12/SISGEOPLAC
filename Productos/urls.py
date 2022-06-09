"""URLs Production"""

#Django
from django.urls import path

#Views
from Productos import views

urlpatterns = [

    #Listas
    path(
        route='listado_productos', 
        view=views.ListaProductoView.as_view(), 
        name='Productos'
    ),
    path(
        route='listado_dimensiones', 
        view=views.ListaDimensiones.as_view(),
        name='Dimensiones'
    ),
    path(
        route='listado_atributos', 
        view=views.ListaAtributos.as_view(),
        name='Atributos'
    ),
    path(
        route='listado_pruebas', 
        view=views.ListaPruebas.as_view(),
        name='Pruebas'
    ),
    path(
        route='listado_normas', 
        view=views.ListaNormas.as_view(),
        name='Normas'
    ),
    #Detalle
    path(
        route='ficha_<int:pk>/',
        view=views.DetalleFichaView.as_view(),
        name='Detalle_ficha'
    ),
    #Actualizar
    path(
        route='actualizar_ficha/<int:pk>/',
        view=views.ActualizarFichaTecnica.as_view(),
        name='Actualizar_ficha_tecnica'
    ),
    #Crear
    path(
        route='nueva_dimension',
        view=views.NuevaDimensionView.as_view(),
        name='Nueva_dimension'
    ),
    path(
        route='nueva_prueba',
        view=views.NuevaPruebaView.as_view(),
        name='Nueva_prueba'
    ),
    path(
        route='nuevo_control',
        view=views.NuevoAtributoView.as_view(),
        name='Nuevo_atributo'
    ),
    path(
        route='nueva_norma',
        view=views.NuevaNormaView.as_view(),
        name='Nueva_norma'
    ),
    path(
        route='nueva_ficha',
        view=views.NuevaFichaTecnica.as_view(),
        name='Nueva_ficha'
    ),
]