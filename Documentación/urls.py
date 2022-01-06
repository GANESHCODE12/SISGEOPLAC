"""URLs de sistema de documentación"""

#Django
from django.urls import path

#Views
from Documentación import views

urlpatterns = [

    path(
        route='documentos/', 
        view=views.DocumentosView.as_view(), 
        name='Documentos'
    ),
    path(
        route='nuevo_documento/', 
        view=views.CrearDocumentoView.as_view(), 
        name='Crear_documento'
    ),
    path(
        route='detalle_documento/<int:pk>/', 
        view=views.DetalleDocumentoView.as_view(), 
        name='Detalle_documento'
    ),
    path(
        route='actualizar_documento/<int:pk>/', 
        view=views.ActualizarDocumento.as_view(), 
        name='Actualizar_documento'
    ),

]