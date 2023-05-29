"""Vistas de la aplicación control de producción"""

# Django
from django.urls import reverse_lazy
from django.db.models import Q
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from datetime import datetime

# Form
from Control_produccion.forms import *

# Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# Models
from Control_produccion.models import *
from Produccion.models import Produccion
from Gestion_Humana.models import TecnicosOperarios

# Utils
import json


class ListaControl(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Control_produccion/lista_controles.html'
    model = ControlProduccion
    permission_required = 'view_controlproduccion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        controles = ControlProduccion.objects.all()[:200]
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in controles:
                    colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id).only('colaborador__nombre')
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.productos.Nombre_producto
                    item['saldo_orden'] = i.saldo_orden
                    item['fecha_creacion'] = i.fecha_creacion
                    item['maquina'] = i.numero_op.maquina
                    item['colaboradores'] = [
                        {'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de controles'
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Controles'
        return context


class ListaMotivosView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de motivos de paradas"""

    template_name = 'Control_produccion/lista_motivos.html'
    model = MotivosParadasControlProduccion
    permission_required = 'view_motivosparadascontrolproduccion'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Motivos De Paradas'
        context['list_url'] = reverse_lazy(
            'Control_produccion:motivos-de-paradas')
        context['entity'] = 'Motivos'
        return context


class CrearNuevoControlView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    template_name = 'Control_produccion/crear_control.html'
    form_class = CrearControlForm
    success_url = reverse_lazy('Control_produccion:Control_orden')
    context_object_name = 'Control_produccion'
    permission_required = 'add_controlproduccion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    control = json.loads(request.POST['control'])
                    produccion = Produccion.objects.get(numero_op=kwargs.get('pk'))
                    control_produccion = ControlProduccion()
                    control_produccion.numero_op_id = kwargs.get('pk')
                    control_produccion.turno = control['turno']
                    control_produccion.hora_inicio = datetime.strptime(
                        control['hora_inicio'], '%d-%m-%Y %H:%M %Z:%S')
                    control_produccion.hora_final = datetime.strptime(
                        control['hora_final'], '%d-%m-%Y %H:%M %Z:%S')
                    control_produccion.cantidad_producida = control['cantidad_producida']
                    control_produccion.ciclo_turno = control['ciclo_turno']
                    control_produccion.cavidades_operacion = control['cavidades_operacion']
                    control_produccion.observaciones = control['observaciones']
                    control_produccion.save(self)
                    control_query = ControlProduccion.objects.filter(
                        numero_op_id=kwargs.get('pk')).aggregate(cantidad_acumulada=Sum('cantidad_producida'))
                    if  produccion.cantidad_requerida - control_query['cantidad_acumulada'] <= 0:
                        produccion.estado_op = 'Terminada'
                        produccion.save()
                    for colaborador in control['colaborador']:
                        modelo_colaborador = ColaboradorControlProduccion()
                        modelo_colaborador.control_id = control_produccion.id
                        modelo_colaborador.colaborador_id = colaborador['id']
                        modelo_colaborador.save(self)
                    for motivo in control['motivo']:
                        modelo_motivo = TiemposParadasControlProduccion()
                        modelo_motivo.control_id = control_produccion.id
                        modelo_motivo.motivo_id = motivo['id']
                        modelo_motivo.horas = int(motivo['horas'])
                        modelo_motivo.minutos = int(motivo['minutos'])
                        modelo_motivo.observacion = motivo['observacion']
                        modelo_motivo.save(self)
            elif action == 'search_colaborador':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                busqueda = TecnicosOperarios.objects.filter(
                    Q(nombre__icontains=request.POST['term']) |
                    Q(codigo__icontains=request.POST['term'])).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'search_motivo':
                data = []
                ids_motivos_exclude = json.loads(request.POST['ids_motivos'])
                busqueda = MotivosParadasControlProduccion.objects.filter(
                    motivo__icontains=request.POST['term']).exclude(id__in=ids_motivos_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.motivo
                    item['minutos'] = 0
                    item['horas'] = 0
                    item['observacion'] = ''
                    data.append(item)
            elif action == 'create_element':
                with transaction.atomic():
                    formElemento = CrearMotivoForm(request.POST)
                    data = formElemento.save(self)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        """Función que agrega el contexto de la información 
        de producción"""

        pk = self.kwargs.get('pk')

        control = ControlProduccion.objects.all().filter(
            numero_op_id=pk).aggregate(numero_op_id=Sum('cantidad_producida'))
        produccion = Produccion.objects.get(pk=pk)

        context = super().get_context_data(**kwargs)
        context['produccion'] = Produccion.objects.get(pk=pk)
        context['title'] = "Nuevo Control"
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Controles'
        context['action'] = 'add'
        context['formElemento'] = CrearMotivoForm()
        context['saldo'] = (produccion.cantidad_requerida - control['numero_op_id']
                            ) if control['numero_op_id'] is not None else produccion.cantidad_requerida
        return context


class NuevoMotivoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear los motivos de paradas"""

    model = MotivosParadasControlProduccion
    form_class = CrearMotivoForm
    permission_required = 'add_motivosparadascontrolproduccion'
    template_name = 'Control_produccion/motivos.html'
    success_url = reverse_lazy('Control_produccion:motivos-de-paradas')

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
        context['title'] = 'Crear Motivo De Parada'
        context['list_url'] = reverse_lazy(
            'Control_produccion:motivos-de-paradas')
        context['entity'] = 'Nuevo Motivo'
        context['action'] = 'add'
        return context


class DetalleControlView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de los controles"""

    template_name = 'Control_produccion/detalle_control.html'
    queryset = ControlProduccion.objects.all()
    context_object_name = 'Control_produccion'
    permission_required = 'view_controlproduccion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        paradas = TiemposParadasControlProduccion.objects.filter(control_id=pk)
        controles = ControlProduccion.objects.filter(id=pk)
        for control in controles:
            context['tiempo_total_parada'] = control.tiempo_total_paradas
            context['tiempo_produccion'] = control.tiempo_produccion
            context['cantidad_esperada_turno'] = control.cantidad_esperada_turno
            context['rendimiento'] = control.rendimiento_produccion
        context['title'] = 'Detalle control'
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Controles'
        context['tecnicos'] = ColaboradorControlProduccion.objects.filter(control_id=pk)
        context['paradas'] = paradas
        return context


class HistoricoControlView(TemplateView):
    template_name = 'Control_produccion/historico_control.html'

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
                search = ControlProduccion.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_actualizacion__range=[start_date, end_date])
                for i in search:
                    colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id).only('colaborador__nombre')
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.productos.Nombre_producto
                    item['saldo_orden'] = i.saldo_orden
                    item['fecha_creacion'] = i.fecha_creacion
                    item['maquina'] = i.numero_op.maquina
                    item['colaboradores'] = [
                        {'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores
                    ]
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historico Controles'
        context['list_url'] = reverse_lazy('Historico')
        context['entity'] = 'Historico'
        context['form'] = HistoricalForm()
        return context


class ReporteControlView(TemplateView):
    template_name = 'Control_produccion/reporte_control.html'

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
                search = Produccion.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_creacion__range=[start_date, end_date])
                for i in search:
                    item = i.toJSON()
                    item['orden'] = i.numero_op
                    item['tiempo_paradas'] = i.tiempo_paradas
                    item['tiempo_produccion'] = i.resta_tiempos
                    item['tiempo_real'] = i.tiempo_produccion
                    item['tiempo_esperado'] = round(timedelta(hours=i.tiempo_esperado).total_seconds(), 2)
                    item['cumplimiento'] = round((i.tiempo_esperado / i.resta_tiempos if i.resta_tiempos is not None else 1) * 100, 2)
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte controles'
        context['list_url'] = reverse_lazy('Reportes')
        context['entity'] = 'Reportes'
        context['form'] = HistoricalForm()
        return context


class ReporteRendimientoView(TemplateView):
    template_name = 'Control_produccion/reporte_rendimiento.html'

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
                search = ColaboradorControlProduccion.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(control__fecha_creacion__range=[start_date, end_date])
                for i in search:
                    item = i.toJSON()
                    item['control'] = i.control_id
                    item['turno'] = i.control.turno
                    item['maquina'] = i.control.numero_op.maquina
                    item['producto'] = i.control.numero_op.producto.productos.Nombre_producto
                    item['numero_op'] = i.control.numero_op_id
                    item['colaborador'] = i.colaborador.nombre
                    item['cargo'] = i.colaborador.cargo
                    item['cantidad_producida'] = i.control.cantidad_producida
                    item['cantidad_esperada'] = round(i.cantidad_esperada_turno, 2)
                    item['rendimiento'] = round(i.rendimiento_produccion, 2)
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte rendimiento'
        context['list_url'] = reverse_lazy('Reportes')
        context['entity'] = 'Reportes'
        context['form'] = HistoricalForm()
        return context


class ReporteParadasView(TemplateView):
    template_name = 'Control_produccion/reporte_paradas.html'

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
                search = TiemposParadasControlProduccion.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(control__fecha_creacion__range=[start_date, end_date])
                for i in search:
                    colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.control_id)
                    item = i.toJSON()
                    item['control'] = i.control_id
                    item['numero_op'] = i.control.numero_op_id
                    item['motivo'] = i.motivo.motivo
                    item['tiempo_paradas'] = i.tiempo_paradas.total_seconds()
                    item['colaboradores'] = [colaborador.colaborador.nombre for colaborador in colaboradores]
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte paradas'
        context['list_url'] = reverse_lazy('Reportes')
        context['entity'] = 'Reportes'
        context['form'] = HistoricalForm()
        return context
