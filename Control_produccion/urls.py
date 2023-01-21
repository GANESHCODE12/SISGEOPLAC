"""URLs Control de producción"""

#Django
from django.urls import path

#Views
from Control_produccion import views

urlpatterns = [

    path(
        route='Control_orden/', 
        view=views.ListaControl.as_view(), 
        name='Control_orden'
    ),
    path(
        route='motivos-de-paradas', 
        view=views.ListaMotivosView.as_view(), 
        name='motivos-de-paradas'
    ),
    path(
        route='nuevo-motivo-de-parada', 
        view=views.NuevoMotivoView.as_view(), 
        name='nuevo-motivo-de-parada'
    ),
    path(
        route='Crear_nuevo_control/<int:pk>/', 
        view=views.CrearNuevoControlView.as_view(), 
        name='Crear_nuevo_control'
    ),
    path(
        route='Detalle_control/<int:pk>/', 
        view=views.DetalleControlView.as_view(), 
        name='Detalle_control'
    ),
    path(
        route='historico-controles', 
        view=views.HistoricoControlView.as_view(), 
        name='historico-controles'
    ),

]