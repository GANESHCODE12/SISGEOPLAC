"""URLs Production"""

#Django
from django.urls import path

#Views
from Produccion import views

urlpatterns = [

    path(
        route='listado_ordenes', 
        view=views.ListaOrdenesView.as_view(), 
        name='Ordenes_produccion'
    ),
    path(
        route='detalle_orden/<int:pk>/',
        view=views.DetalleOrdenView.as_view(),
        name='Detalle_orden'
    ),
    path(
        route='nueva_orden/<int:pk>',
        view=views.CrearOrdenView.as_view(),
        name='Nueva_orden'
    ),
    path(
        route='actualizar/orden-<int:pk>/notificacion-<int:Notificacion_id>', 
        view=views.ActualizarOrdenNotificacionView.as_view(), 
        name='actualizar-orden-notificacion'
    ),
    path(
        route='actualizar/orden-<int:pk>', 
        view=views.ActualizarOrdenView.as_view(), 
        name='actualizar-orden'
    ),
    path(
        route='nuevo-desarrollo', 
        view=views.CrearDesarrolloView.as_view(), 
        name='nuevo-desarrollo'
    ),
    path(
        route='historico-ordenes', 
        view=views.HistoricoOrdenView.as_view(), 
        name='historico-ordenes'
    ),
    path(
        route='detalle-historico-ordenes/orden-<int:pk>', 
        view=views.DetalleHistoricoOrdenView.as_view(), 
        name='detalle-historico-ordenes'
    ),
]