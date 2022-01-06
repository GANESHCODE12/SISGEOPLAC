"""URLs Quality control"""

#Django
from django.urls import path

#Views
from Control_calidad import views

urlpatterns = [

    path(
        route='Inspecciones_calidad/', 
        view=views.ListaInspecciones.as_view(), 
        name='Inspecciones_calidad'
    ),
    path(
        route='Detalle_inspeccion/<int:pk>', 
        view=views.DetalleInspeccion.as_view(), 
        name='Detalle_inspeccion'
    ),
    path(
        route='Certificado_calidad/<int:pk>', 
        view=views.CertificadoCalidad.as_view(), 
        name='Certificado_calidad'
    ),
    path(
        route='Actualizar_certificado/<int:pk>', 
        view=views.ActualizarCertificado.as_view(), 
        name='Actualizar_certificado'
    ),
    path(
        route='Crear_inspeccion/<int:pk>', 
        view=views.CrearInspeccionView.as_view(), 
        name='Nueva_inspeccion'
    ),

]