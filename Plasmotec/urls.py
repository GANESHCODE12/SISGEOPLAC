"""Plasmotec URL Configuration"""

#Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

#Views
from Plasmotec import views

urlpatterns = [

    #Inicio
    path(
        route = '',
        view= views.InicioView.as_view(),
        name='inicio'
    ),
    #test
    path(
        route = 'test/',
        view= views.TestView.as_view(),
        name='test'
    ),
    #Notificación leida
    path(
        route = 'notificacion-leida',
        view= views.NotificacionLeida.as_view(),
        name='notificacion-leida'
    ),
    #Notificaciones
    path(
        route = 'Notificaciones',
        view= views.Notificaciones.as_view(),
        name='Notificaciones'
    ),
    #Notificaciones
    path(
        route = 'Reportes',
        view= views.ReporteView.as_view(),
        name='Reportes'
    ),
    path(
        route = 'Historico',
        view= views.HistoricoView.as_view(),
        name='Historico'
    ),
    path(
        route='diagrama-gantt',
        view=views.DiagramaGantt.as_view(),
        name='diagrama-gantt'
    ),
    
    #Admin urls
    path('admin/', admin.site.urls),

    #Users urls
    path(
        'users/', 
        include(
            ('users.urls', 'users'), 
            namespace='users'
        )
    ),

    #App_urls
    path(
        'produccion/', 
        include(
            ('Produccion.urls', 'Produccion'), 
            namespace='Produccion'
            )
    ),
    path(
        'productos/', 
        include(
            ('Productos.urls', 'Productos'), 
            namespace='Productos'
            )
    ),
    path(
        'Documentación/', 
        include(
            ('Documentación.urls', 'Documentación'), 
            namespace='Documentación'
            )
    ),
    path(
        'Control_produccion/', 
        include(
            ('Control_produccion.urls', 'Control_produccion'), 
            namespace='Control_produccion'
            )
    ),
    path(
        'Producto_no_conforme/', 
        include(
            ('PNC.urls', 'PNC'), 
            namespace='PNC'
            )
    ),
    path(
        'Control_calidad/', 
        include(
            ('Control_calidad.urls', 'Control_calidad'), 
            namespace='Control_calidad'
            )
    ),
    path(
        'Inventario/', 
        include(
            ('Inventario.urls', 'Inventario'), 
            namespace='Inventario'
            )
    ),
    path(
        'Gestión_humana/', 
        include(
            ('Gestion_Humana.urls', 'Gestion_Humana'), 
            namespace='Gestion_humana'
            )
    ),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)