"""URLs de sistema de inventario"""

#Django
from django.urls import path

#Views
from Inventario import views

urlpatterns = [
    path(
        route='Lista_elementos_MP_insumos/', 
        view=views.ListaElementosMPInsumos.as_view(), 
        name='Lista_Elementos_MP_Insumos'
    ),
    path(
        route='Ingreso_MP_insumos/', 
        view=views.EntradaMPView.as_view(), 
        name='Ingresos_MP_Insumos'
    ),
    path(
        route='Requisicion_MP_insumos/<int:pk>', 
        view=views.Requision_MP_I.as_view(), 
        name='Requisicion_MP_I'
    ),
    path(
        route='Reporte_MPI/', 
        view=views.ReportMPIView.as_view(), 
        name='Reporte_MPI'
    ),
    path(
        route='Inventario_PT/', 
        view=views.ListaProductoTerminado.as_view(), 
        name='Inventario_PT'
    ),
    path(
        route='inventario-producto-terminado-orden/', 
        view=views.ListaProductoTerminadoOrden.as_view(), 
        name='inventario-producto-terminado-orden'
    ),
    path(
        route='Requisición_PT/', 
        view=views.Requision_PT_View.as_view(), 
        name='Requisicion_PT'
    ),
    path(
        route='Reporte_PT/', 
        view=views.ReportPTView.as_view(), 
        name='Reporte_PT'
    ),
    path(
        route='Ingresos/', 
        view=views.Ingresos.as_view(), 
        name='Ingresos'
    ),
]