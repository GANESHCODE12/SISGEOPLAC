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
        route='actualizar_orden/<int:pk>/', 
        view=views.ActualizarOrden.as_view(), 
        name='actualizar'
    ),
    
]