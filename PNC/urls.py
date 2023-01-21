"""URLs PNC"""

#Django
from django.urls import path

#Views
from PNC import views

urlpatterns = [

    path(
        route='Productos_no_conformes/', 
        view=views.ListaPNC.as_view(), 
        name='Productos_no_conformes'
    ),
    path(
        route='motivos-pnc', 
        view=views.ListaMotivosPncView.as_view(), 
        name='motivos-pnc'
    ),
    path(
        route='Nuevo_producto_no_conforme/<int:pk>', 
        view=views.NuevoPncView.as_view(), 
        name='Nuevo_PNC'
    ),
    path(
        route='motivo-pnc', 
        view=views.NuevoMotivoView.as_view(), 
        name='motivo-pnc'
    ),
    path(
        route='Detalle_PNC/<int:pk>', 
        view=views.DetallePncView.as_view(), 
        name='Detalle_PNC'
    ),
    path(
        route='actualizar_pnc/<int:pk>/', 
        view=views.ActualizarPNC.as_view(), 
        name='Actualizar_PNC'
    ),
    path(
        route='reporte-producto-no-conforme', 
        view=views.ReportPncView.as_view(), 
        name='reporte-producto-no-conforme'
    ),

]