"""Vistas de la aplicación Producto no conforme"""

# Django
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

# Form
from PNC.forms import ActualizarPNC, CrearPncForm, MotivoForm, ReportPncForm

# Models
from PNC.models import MotivoPnc, ProductoNoConforme, TrazabilidadProductoNoConforme
from Control_calidad.models import ControlCalidad, ColaboradorInspeccionCalidad

# Utils
import json


class ListaPNC(LoginRequiredMixin, ListView):
    """Vista para la vista de lista de controles"""

    template_name = 'PNC/lista_pnc.html'
    model = ProductoNoConforme

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ProductoNoConforme.objects.all():
                    colaboradores = ColaboradorInspeccionCalidad.objects.filter(inspeccion_id=i.id)
                    item = i.toJSON()
                    item['numero_op'] = i.id_inspeccion.numero_op_id
                    item['producto'] = i.id_inspeccion.numero_op.producto.productos.Nombre_producto
                    item['color'] = i.id_inspeccion.numero_op.producto.color.color
                    item['inspector'] = i.inspector_calidad.get_full_name()
                    item['turno'] = i.id_inspeccion.turno
                    item['colaboradores'] = [{'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                    item['tipo_pnc'] = i.tipo_pnc.motivo
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Producto no conforme'
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        return context


class NuevoPncView(LoginRequiredMixin, CreateView):
    """Vista para crear los productos no conformes"""

    template_name = 'PNC/crear_pnc.html'
    form_class = CrearPncForm
    success_url = reverse_lazy('PNC:Productos_no_conformes')
    context_object_name = 'ProductoNoConforme'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    pnc_post = json.loads(request.POST['pnc'])
                    for pnc in pnc_post['pnc_post']:
                        pnc_model = ProductoNoConforme()
                        pnc_model.id_inspeccion_id = kwargs.get('pk')
                        pnc_model.tipo_pnc_id = pnc['id']
                        pnc_model.estado_pnc = pnc['estado_pnc']
                        pnc_model.cantidad_pnc = pnc['cantidad_pnc']
                        pnc_model.observaciones = pnc['observaciones']
                        pnc_model.save(self)
                    for pnc in pnc_post['pnc_post']:
                        pnc_trazabilidad = TrazabilidadProductoNoConforme()
                        pnc_trazabilidad.id_inspeccion_id = kwargs.get('pk')
                        pnc_trazabilidad.tipo_pnc_id = pnc['id']
                        pnc_trazabilidad.estado_pnc = pnc['estado_pnc']
                        pnc_trazabilidad.cantidad_pnc = pnc['cantidad_pnc']
                        pnc_trazabilidad.observaciones = pnc['observaciones']
                        pnc_trazabilidad.save(self)
            elif action == 'search_motivo':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                busqueda = MotivoPnc.objects.filter(
                    motivo__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.motivo
                    item['id_pnc'] = ''
                    item['observaciones'] = ''
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        """Función que agrega al contexto la información 
        de producción y control producción"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['control_calidad'] = ControlCalidad.objects.get(pk=pk)
        context['pnc'] = ProductoNoConforme.objects.all().filter(
            id_inspeccion=pk)
        context['title'] = "Nuevo Producto No Conforme"
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        context['action'] = 'add'
        return context


class DetallePncView(LoginRequiredMixin, DetailView):
    """Vista para el detalle de las ordenes"""

    template_name = 'PNC/detalle_pnc.html'
    queryset = ProductoNoConforme.objects.all()
    context_object_name = 'ProductoNoConforme'

    def get_context_data(self, **kwargs):
        """Función que agrega al contexto la información 
        de producción y control producción"""

        pk = self.kwargs.get('pk')
        pnc = ProductoNoConforme.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['tecnicos'] = ColaboradorInspeccionCalidad.objects.filter(
            inspeccion=pnc.id_inspeccion)
        context['title'] = 'Detalle PNC'
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        return context


class ActualizarPNC(LoginRequiredMixin, TemplateView):
    """Vista para actualizar el PNC"""

    template_name = 'PNC/crear_pnc.html'
    model = ProductoNoConforme
    success_url = reverse_lazy('PNC:Productos_no_conformes')
    form_class = ActualizarPNC
    context_object_name = 'ProductoNoConforme'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_pnc(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            pnc_detalle = ProductoNoConforme.objects.filter(id_inspeccion=pk)

            for pnc in pnc_detalle:
                item = pnc.toJSON()
                item['id'] = pnc.tipo_pnc_id
                item['id_pnc'] = pnc.id
                item['text'] = pnc.tipo_pnc.motivo
                item['estado_pnc'] = pnc.estado_pnc
                item['cantidad_pnc'] = pnc.cantidad_pnc
                item['observaciones'] = pnc.observaciones
                data.append(item)
        except Exception as exc:
            print(exc)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                with transaction.atomic():
                    pnc_post = json.loads(request.POST['pnc'])
                    for pnc in pnc_post['pnc_post']:
                        if pnc['id_pnc'] != '':
                            pnc_model = ProductoNoConforme.objects.get(
                                id=pnc['id_pnc'])
                        else:
                            pnc_model = ProductoNoConforme()
                        pnc_model.id_inspeccion_id = kwargs.get('pk')
                        pnc_model.tipo_pnc_id = pnc['id']
                        pnc_model.estado_pnc = pnc['estado_pnc']
                        pnc_model.cantidad_pnc = pnc['cantidad_pnc']
                        pnc_model.observaciones = pnc['observaciones']
                        pnc_model.save(self)
                    for pnc in pnc_post['pnc_post']:
                        pnc_trazabilidad = TrazabilidadProductoNoConforme()
                        pnc_trazabilidad.id_inspeccion_id = kwargs.get('pk')
                        pnc_trazabilidad.tipo_pnc_id = pnc['id']
                        pnc_trazabilidad.estado_pnc = pnc['estado_pnc']
                        pnc_trazabilidad.cantidad_pnc = pnc['cantidad_pnc']
                        pnc_trazabilidad.observaciones = pnc['observaciones']
                        pnc_trazabilidad.save(self)
            elif action == 'search_motivo':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                busqueda = MotivoPnc.objects.filter(
                    motivo__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.motivo
                    item['id_pnc'] = ''
                    item['observaciones'] = ''
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['control_calidad'] = ControlCalidad.objects.get(pk=pk)
        context['pnc'] = ProductoNoConforme.objects.all().filter(
            id_inspeccion=pk)
        context['title'] = 'Actualizar PNC'
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        context['action'] = 'edit'
        context['pnc'] = json.dumps(self.get_pnc())
        return context


class NuevoMotivoView(LoginRequiredMixin, CreateView):

    model = MotivoPnc
    form_class = MotivoForm
    template_name = 'PNC/motivo_pnc.html'
    success_url = reverse_lazy('PNC:motivos-pnc')

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
        context['title'] = 'Motivos de productos no conformes'
        context['list_url'] = reverse_lazy('PNC:motivos-pnc')
        context['entity'] = 'PNC'
        context['action'] = 'add'
        return context


class ListaMotivosPncView(LoginRequiredMixin, ListView):

    template_name = 'PNC/lista_motivos_pnc.html'
    model = MotivoPnc

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de motivos pnc'
        context['list_url'] = reverse_lazy('PNC:motivos-pnc')
        context['entity'] = 'Motivos PNC'
        return context


class ReportPncView(TemplateView):
    template_name = 'PNC/report_pnc.html'

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
                search = ProductoNoConforme.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_actualizacion__range=[start_date, end_date])
                for i in search:
                    colaboradores = ColaboradorInspeccionCalidad.objects.filter(inspeccion_id=i.id)
                    data.append([
                        i.id_inspeccion.numero_op.producto.productos.Nombre_producto,
                        i.id_inspeccion.numero_op.producto.color.color,
                        i.tipo_pnc.motivo,
                        i.fecha_actualizacion.strftime("%d/%m/%Y"),
                        i.id_inspeccion.numero_op_id,
                        i.id_inspeccion_id,
                        i.estado_pnc,
                        i.cantidad_pnc,
                        [colaborador.colaborador.nombre for colaborador in colaboradores],
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte producto no conforme'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('Reportes')
        context['form'] = ReportPncForm()
        return context
