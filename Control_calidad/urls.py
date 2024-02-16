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
        route='certificados-calidad/', 
        view=views.ListaCertificados.as_view(), 
        name='certificados-calidad'
    ),
    path(
        route='Detalle_inspeccion/<int:pk>', 
        view=views.DetalleInspeccion.as_view(), 
        name='Detalle_inspeccion'
    ),
    path(
        route='Certificado_calidad/<int:pk>', 
        view=views.CertificadoCalidadView.as_view(), 
        name='Certificado_calidad'
    ),
    path(
        route='Crear_inspeccion/<int:pk>', 
        view=views.CrearInspeccionView.as_view(), 
        name='Nueva_inspeccion'
    ),
    path(
        route='crear-certificado-calidad/<int:pk>', 
        view=views.CrearCertificadoView.as_view(), 
        name='crear-certificado-calidad'
    ),
    path(
        route='crear-inspeccion-mp/<int:pk>', 
        view=views.InspeccionMPView.as_view(), 
        name='crear-inspeccion-mp'
    ),
    path(
        route='detalle-inspeccion-mp/<int:pk>', 
        view=views.DetalleInspeccionMpView.as_view(), 
        name='detalle-inspeccion-mp'
    ),
    path(
        route='actualizar-inspeccion-mp/<int:pk>', 
        view=views.ActualizarInspeccionMPView.as_view(), 
        name='actualizar-inspeccion-mp'
    ),
    path(
        route='historico-inspecciones', 
        view=views.HistoricoInspeccionView.as_view(), 
        name='historico-inspecciones'
    ),

]