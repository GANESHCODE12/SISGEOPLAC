"""Vistas de la aplicación de gestión humana"""

# Django
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Form
from Gestion_Humana.forms import *

# Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# Models
from Gestion_Humana.models import *


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
