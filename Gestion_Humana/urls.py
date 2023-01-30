"""URLs Gestión humana"""

#Django
from django.urls import path

#Views
from Gestion_Humana import views

urlpatterns = [

    path(
        route='Nuevo_colaborador/', 
        view=views.NuevaColaboradorView.as_view(), 
        name='Nuevo_colaborador'
    ),
    path(
        route='tecnicos-operarios/', 
        view=views.NuevoTecnicoOperarioView.as_view(), 
        name='tecnicos-operarios'
    ),
    path(
        route='Colaboradores/', 
        view=views.ColaboradoresView.as_view(), 
        name='Colaboradores'
    ),
    path(
        route='lista-tecnicos-operarios/', 
        view=views.TecnicosOperariosView.as_view(), 
        name='lista-tecnicos-operarios'
    ),
    path(
        route='reporte-colaboradores/', 
        view=views.ReportColaboradoresView.as_view(), 
        name='reporte-colaboradores'
    ),
    path(
        route='Otro_si/<int:pk>/', 
        view=views.OtroSiView.as_view(), 
        name='Otro_si'
    ),
    path(
        route='Actualizar_colaborador/<int:pk>', 
        view=views.ActualizarColaborador.as_view(), 
        name='Actualizar_colaborador'
    ),
    path(
        route='Proceso_disciplinario/<int:pk>', 
        view=views.ProcesoDisciplinarioView.as_view(), 
        name='Proceso_disciplinario'
    ),
    path(
        route='Actualizar_otro_si/<int:pk>', 
        view=views.ActualizarOtroSiView.as_view(), 
        name='Actualizar_otro_si'
    ),
    path(
        route='Actualizar_proceso_disciplinario/<int:pk>', 
        view=views.ActualizarProceso.as_view(), 
        name='Actualizar_proceso_disciplinario'
    ),
    path(
        route='Colaborador/<int:pk>', 
        view=views.ColaboradorView.as_view(), 
        name='Colaborador'
    ),
    path(
        route='examenes-medicos/<int:pk>', 
        view=views.ExamenesMedicosView.as_view(), 
        name='examenes-medicos'
    ),
    path(
        route='entrega-dotacion/<int:pk>', 
        view=views.EntregaDotacionView.as_view(), 
        name='entrega-dotacion'
    ),
    path(
        route='capacitacion/<int:pk>', 
        view=views.CapacitacionView.as_view(), 
        name='capacitacion'
    ),
    path(
        route='actualizar-examen-medico/<int:pk>', 
        view=views.ActualizarExamenesView.as_view(), 
        name='actualizar-examen-medico'
    ),
    path(
        route='actualizar-capacitacion/<int:pk>', 
        view=views.ActualizarCapacitacionView.as_view(), 
        name='actualizar-capacitacion'
    ),
    path(
        route='actualizar-entrega-dotacion/<int:pk>', 
        view=views.ActualizarDotacionView.as_view(), 
        name='actualizar-entrega-dotacion'
    ),

]