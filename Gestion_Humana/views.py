"""Vistas de la aplicación de gestión humana"""

# Django
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.db.models import Q

# Form
from Gestion_Humana.forms import *

# Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# Models
from Gestion_Humana.models import *

# Utils
import json
from datetime import datetime


class NuevaColaboradorView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    model = InformacionColaborador
    form_class = NuevoColaboradorForm
    template_name = 'Gestion_Humana/nuevo_colaborador.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_informacioncolaborador'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Colaborador'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        return context


class ColaboradoresView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Gestion_Humana/lista_colaboradores.html'
    model = InformacionColaborador
    permission_required = 'view_informacioncolaborador'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in InformacionColaborador.objects.all():
                    item = i.toJSON()
                    item['full_name'] = i.nombres + ' ' + i.apellidos
                    data.append(item)
            elif action == 'search_details_otro_si':
                data = []
                for i in OtroSi.objects.filter(colaborador_id=request.POST['id']):
                    item = i.toJSON()
                    item['otro_si'] = i.get_otro_si()
                    data.append(item)
            elif action == 'search_details_procesos':
                data = []
                for i in ProcesosDisciplinarios.objects.filter(colaborador_id=request.POST['id']):
                    item = i.toJSON()
                    item['carta_citacion'] = i.get_carta_citacion()
                    item['acta'] = i.get_acta()
                    data.append(item)
            elif action == 'search_details_examen':
                data = []
                for i in ExamenesMedicos.objects.filter(colaborador_id=request.POST['id']):
                    item = i.toJSON()
                    item['resultados'] = i.get_resultados()
                    data.append(item)
            elif action == 'search_details_capacitacion':
                data = []
                for i in Capacitacion.objects.filter(colaborador_id=request.POST['id']):
                    item = i.toJSON()
                    item['certificado'] = i.get_certificado()
                    data.append(item)
            elif action == 'search_details_dotacion':
                data = []
                for i in EntregaDotacion.objects.filter(colaborador_id=request.POST['id']):
                    item = i.toJSON()
                    item['documento'] = i.get_documento_entrega()
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Colaboradores'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        return context


class OtroSiView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = OtroSi
    form_class = OtroSiForm
    template_name = 'Gestion_Humana/otro_si.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_otrosi'

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_Otro_si = form.save(commit=False)
        instance_Otro_si.colaborador = self.instance_Colaborador
        instance_Otro_si.save()

        return super(OtroSiView, self).form_valid(form)

    def get(self, request, *args, **kwargs):

        self.instance_Colaborador = get_object_or_404(
            InformacionColaborador, pk=kwargs.get('pk'))
        return super(OtroSiView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Colaborador = get_object_or_404(
                    InformacionColaborador, pk=kwargs.get('pk'))
                super(OtroSiView, self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Otro Si'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        context['colaborador'] = InformacionColaborador.objects.get(pk=pk)
        return context


class ActualizarColaborador(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_colaborador.html'
    model = InformacionColaborador
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarColaboradorForm
    context_object_name = 'InformacionColaborador'
    permission_required = 'change_informacioncolaborador'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Información del Colaborador: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class ProcesoDisciplinarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = ProcesosDisciplinarios
    form_class = ProcesosDisciplinariosForm
    template_name = 'Gestion_Humana/procesos_disciplinarios.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_procesosdisciplinarios'

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_Proceso_disciplinario = form.save(commit=False)
        instance_Proceso_disciplinario.colaborador = self.instance_Colaborador
        instance_Proceso_disciplinario.save()

        return super(ProcesoDisciplinarioView, self).form_valid(form)

    def get(self, request, *args, **kwargs):

        self.instance_Colaborador = get_object_or_404(
            InformacionColaborador, pk=kwargs.get('pk'))
        return super(ProcesoDisciplinarioView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Colaborador = get_object_or_404(
                    InformacionColaborador, pk=kwargs.get('pk'))
                super(ProcesoDisciplinarioView, self).post(
                    request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Proceso Disciplinario'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        context['colaborador'] = InformacionColaborador.objects.get(pk=pk)
        return context


class ActualizarOtroSiView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_otro_si.html'
    model = OtroSi
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarOtroSiForm
    context_object_name = 'OtroSi'
    permission_required = 'change_otrosi'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Otro Si: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class ActualizarProceso(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_proceso.html'
    model = ProcesosDisciplinarios
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarProcesosDisciplinariosForm
    context_object_name = 'ProcesosDisciplinarios'
    permission_required = 'change_procesosdisciplinarios'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Proceso Disciplinario: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class ColaboradorView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las fichas técnicas"""

    model = InformacionColaborador
    template_name = 'Gestion_Humana/colaborador.html'
    queryset = InformacionColaborador.objects.all()
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    context_object_name = 'Colaborador'
    permission_required = 'view_informacioncolaborador'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['OtroSi'] = OtroSi.objects.all().filter(colaborador_id=pk)
        context['ProcesosDiscliplinarios'] = ProcesosDisciplinarios.objects.all(
        ).filter(colaborador_id=pk)
        context['title'] = 'Colaborador'
        context['entity'] = 'Colaboradores'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        return context


class NuevoTecnicoOperarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    model = TecnicosOperarios
    form_class = TecnicoForm
    template_name = 'Gestion_Humana/nuevo_tecnico.html'
    success_url = reverse_lazy('Gestion_Humana:lista-tecnicos-operarios')
    permission_required = 'add_tecnicosoperarios'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo técnico y/o operario'
        context['list_url'] = reverse_lazy(
            'Gestion_Humana:lista-tecnicos-operarios')
        context['entity'] = 'Tecnicos Operarios'
        context['action'] = 'add'
        return context


class TecnicosOperariosView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Gestion_Humana/tecnicosoperarios.html'
    model = TecnicosOperarios
    permission_required = 'view_tecnicosoperarios'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in TecnicosOperarios.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Técnios & Operarios'
        context['list_url'] = reverse_lazy(
            'Gestion_Humana:lista-tecnicos-operarios')
        context['entity'] = 'Técnicos & Operarios'
        return context


class ReportColaboradoresView(TemplateView):
    template_name = 'Gestion_Humana/report_colaboradores.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = InformacionColaborador.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_actualizacion__range=[start_date, end_date])
                for i in search:
                    data.append([
                        '{} {}'.format(i.nombres, i.apellidos),
                        i.cargo,
                        i.jefe_inmediato,
                        i.nombre_emergencia,
                        i.parentezco,
                        i.telefono_emergencia,
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte colaboradores'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('Reportes')
        context['form'] = ReportGestionHumanaForm()
        return context


class EntregaDotacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = EntregaDotacion
    form_class = EntregaDotacionForm
    template_name = 'Gestion_Humana/entrega_dotacion.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_entregadotacion'

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_EntregaDotacion = form.save(commit=False)
        instance_EntregaDotacion.colaborador = self.instance_Colaborador
        instance_EntregaDotacion.save()

        return super(EntregaDotacionView, self).form_valid(form)

    def get(self, request, *args, **kwargs):

        self.instance_Colaborador = get_object_or_404(
            InformacionColaborador, pk=kwargs.get('pk'))
        return super(EntregaDotacionView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Colaborador = get_object_or_404(InformacionColaborador, pk=kwargs.get('pk'))
                super(EntregaDotacionView, self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Entrega Dotación'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        context['colaborador'] = InformacionColaborador.objects.get(pk=pk)
        return context


class CapacitacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = Capacitacion
    form_class = CapacitacionForm
    template_name = 'Gestion_Humana/capacitacion.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_capacitacion'

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_Capacitacion = form.save(commit=False)
        instance_Capacitacion.colaborador = self.instance_Colaborador
        instance_Capacitacion.save()

        return super(CapacitacionView, self).form_valid(form)

    def get(self, request, *args, **kwargs):

        self.instance_Colaborador = get_object_or_404(InformacionColaborador, pk=kwargs.get('pk'))
        return super(CapacitacionView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Colaborador = get_object_or_404(InformacionColaborador, pk=kwargs.get('pk'))
                super(CapacitacionView, self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Capacitación'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        context['colaborador'] = InformacionColaborador.objects.get(pk=pk)
        return context


class ExamenesMedicosView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = ExamenesMedicos
    form_class = ExamenesMedicosForm
    template_name = 'Gestion_Humana/examenes_medicos.html'
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    permission_required = 'add_examenesmedicos'

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_ExamenesMedicos = form.save(commit=False)
        instance_ExamenesMedicos.colaborador = self.instance_Colaborador
        instance_ExamenesMedicos.save()

        return super(ExamenesMedicosView, self).form_valid(form)

    def get(self, request, *args, **kwargs):

        self.instance_Colaborador = get_object_or_404(InformacionColaborador, pk=kwargs.get('pk'))
        return super(ExamenesMedicosView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Colaborador = get_object_or_404(InformacionColaborador, pk=kwargs.get('pk'))
                super(ExamenesMedicosView, self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Examen Médico'
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'add'
        context['colaborador'] = InformacionColaborador.objects.get(pk=pk)
        return context


class ActualizarExamenesView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_examenes.html'
    model = ExamenesMedicos
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarExamenForm
    context_object_name = 'ExamenesMedicos'
    permission_required = 'change_examenesmedicos'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Exámen Médico: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class ActualizarCapacitacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_capacitacion.html'
    model = Capacitacion
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarCapacitacionForm
    context_object_name = 'Capacitacion'
    permission_required = 'change_capacitacion'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Capacitación: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class ActualizarDotacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    template_name = 'Gestion_Humana/actualizar_dotacion.html'
    model = EntregaDotacion
    success_url = reverse_lazy('Gestion_Humana:Colaboradores')
    form_class = ActualizarDotacionForm
    context_object_name = 'EntregaDotacion'
    permission_required = 'change_entregadotacion'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Entrega Dotación: '
        context['list_url'] = reverse_lazy('Gestion_Humana:Colaboradores')
        context['entity'] = 'Colaboradores'
        context['action'] = 'edit'
        return context


class CrearProgramacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    template_name = 'Gestion_Humana/crear_programacion.html'
    form_class = CrearProgramacionForm
    success_url = reverse_lazy('Gestion_Humana:programacion-historico')
    context_object_name = 'Programacion'
    permission_required = 'add_programacion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    programacion_form = json.loads(request.POST['programacion'])
                    for colab in programacion_form['programacion_colaborador']:
                        programacion_model = Programacion()
                        programacion_model.colaborador_id = colab['id']
                        programacion_model.turno = colab['turno']
                        programacion_model.fecha_programacion = datetime.strptime(
                            colab['fecha_programacion'], '%Y-%m-%d')
                        programacion_model.maquina = colab['maquina']
                        programacion_model.save(self)
            elif action == 'search_colaborador':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                busqueda = TecnicosOperarios.objects.filter(
                    Q(nombre__icontains=request.POST['term']) |
                    Q(codigo__icontains=request.POST['term']))
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        """Función que agrega el contexto de la información 
        de producción"""

        pk = self.kwargs.get('pk')

        context = super().get_context_data(**kwargs)
        context['title'] = "Programación"
        context['list_url'] = reverse_lazy('Gestion_Humana:programacion-historico')
        context['entity'] = 'Programación'
        context['action'] = 'add'
        return context


class ProgramacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Gestion_Humana/programacion.html'
    model = Programacion
    permission_required = 'view_programacion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Programacion.objects.all().select_related('colaborador'):
                    item = i.toJSON()
                    item['nombre'] = i.colaborador.nombre
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Programacion'
        context['list_url'] = reverse_lazy('Gestion_Humana:programacion')
        context['entity'] = 'Programacion'
        return context


class ActualizarProgramacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, TemplateView):

    template_name = 'Gestion_Humana/actualizar_programacion.html'
    form_class = ActualizarProgramacionForm
    success_url = reverse_lazy('Control_produccion:Control_orden')
    context_object_name = 'Programacion'
    permission_required = 'change_programacion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    programacion_form = json.loads(request.POST['programacion'])
                    for colab in programacion_form['programacion_colaborador']:
                        programacion_model = Programacion.objects.get(id=colab['id'])
                        programacion_model.colaborador_id = colab['colaborador']
                        programacion_model.turno = colab['turno']
                        programacion_model.fecha_programacion = datetime.strptime(
                            colab['fecha_programacion'], '%Y-%m-%d')
                        programacion_model.maquina = colab['maquina']
                        if colab['cumplimiento'] == 1:
                            programacion_model.cumplimiento = True
                        else:
                            programacion_model.cumplimiento = False
                        programacion_model.motivo_incumplimiento = colab['motivo_incumplimiento']
                        programacion_model.turno_reprogramacion = colab['turno_reprogramacion']
                        programacion_model.save()
            elif action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Programacion.objects.all()
                if len(start_date) and len(end_date):
                    search = Programacion.objects.filter(
                        fecha_programacion__range=[start_date, end_date]
                    ).select_related('colaborador')
                action = request.POST['action']
                for i in search:
                    item = i.toJSON()
                    item['nombre'] = i.colaborador.nombre
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        """Función que agrega el contexto de la información 
        de producción"""

        pk = self.kwargs.get('pk')

        context = super().get_context_data(**kwargs)
        context['title'] = "Actualizar programación"
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Actualizar programación'
        context['action'] = 'add'
        context['form'] = ReportGestionHumanaForm()
        return context


class ProgramacionImprimirView(LoginRequiredMixin, ValidatePermissionRequiredMixin, TemplateView):

    template_name = 'Gestion_Humana/programacion_imprimir.html'
    model = Programacion
    permission_required = 'view_programacion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Programacion.objects.all()
                if len(start_date) and len(end_date):
                    search = Programacion.objects.filter(
                        fecha_programacion__range=[start_date, end_date]
                    ).select_related('colaborador')
                action = request.POST['action']
                for i in search:
                    item = i.toJSON()
                    item['nombre'] = i.colaborador.nombre
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Imprimir Programación'
        context['list_url'] = reverse_lazy('Gestion_Humana:imprimir-programacion')
        context['entity'] = 'Imprimir Programación'
        context['form'] = ReportGestionHumanaForm()
        return context
