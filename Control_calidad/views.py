"""Vistas de la aplicación Inspecciones de calidad"""

#Django
from typing import List
from django.http.response import JsonResponse
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#Form
from Control_calidad.forms import *

#Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

#Models
from Control_calidad.models import *
from Productos.models import *
from Produccion.models import Produccion
from Gestion_Humana.models import TecnicosOperarios
from Control_produccion.models import ColaboradorControlProduccion
from Inventario.models import Requisicion
from PNC.models import ProductoNoConforme, TrazabilidadProductoNoConforme

#Utilidades
import json
from datetime import timedelta, datetime, timezone


class ListaInspecciones(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para la vista de lista de controles"""

    model = ControlCalidad
    template_name = 'Control_calidad/lista_inspecciones.html'
    permission_required = 'view_controlcalidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                inspecciones_calidad = ControlCalidad.objects.all()[:200]
                for i in inspecciones_calidad:
                    colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id)
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.productos.Nombre_producto
                    item['cliente'] = i.numero_op.cliente
                    item['maquina'] = i.numero_op.maquina
                    item['lote'] = '{}-{}'.format(i.numero_op_id, i.numero_op.fecha_creacion.year)
                    item['fecha_creacion'] = i.fecha_creacion
                    item['inspector'] = i.inspector.get_full_name()
                    item['colaboradores'] = [{'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                    item['pnc'] = ProductoNoConforme.objects.filter(id_inspeccion=i.id).count()
                    data.append(item)
            elif action == 'search_details_pnc':
                data = []
                for pnc in TrazabilidadProductoNoConforme.objects.filter(id_inspeccion = request.POST['id_inspeccion']):
                    item = pnc.toJSON()
                    item['numero_op'] = pnc.id_inspeccion.numero_op_id
                    item['inspector'] = pnc.inspector_calidad.get_full_name()
                    item['turno'] = pnc.id_inspeccion.turno
                    item['tipo_pnc'] = pnc.tipo_pnc.motivo
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de inspecciones de calidad'
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        return context


class DetalleInspeccion(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las fichas técnicas"""

    model = ControlCalidad
    queryset = ControlCalidad.objects.all()
    template_name = 'Control_calidad/detalle_inspección.html'
    permission_required = 'view_controlcalidad'
    context_object_name = 'ControlCalidad'

    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        inspeccion = ControlCalidad.objects.get(id=pk)
        inspeccion_dimensional = InspeccionDimensional.objects.filter(id_inspeccion_d = pk)
        muestras_dimensional = {}

        for dimension in inspeccion_dimensional:
            if dimension.cavidad_1 is not None:
                muestras_dimensional['cavidad_1'] = dimension.cavidad_1
            if dimension.cavidad_2 is not None:
                muestras_dimensional['cavidad_2'] = dimension.cavidad_2
            if dimension.cavidad_3 is not None:
                muestras_dimensional['cavidad_3'] = dimension.cavidad_3
            if dimension.cavidad_4 is not None:
                muestras_dimensional['cavidad_4'] = dimension.cavidad_4
            if dimension.cavidad_5 is not None:
                muestras_dimensional['cavidad_5'] = dimension.cavidad_5
            if dimension.cavidad_6 is not None:
                muestras_dimensional['cavidad_6'] = dimension.cavidad_6
            if dimension.cavidad_7 is not None:
                muestras_dimensional['cavidad_7'] = dimension.cavidad_7
            if dimension.cavidad_8 is not None:
                muestras_dimensional['cavidad_8'] = dimension.cavidad_8
            if dimension.cavidad_9 is not None:
                muestras_dimensional['cavidad_9'] = dimension.cavidad_9
            if dimension.cavidad_10 is not None:
                muestras_dimensional['cavidad_10'] = dimension.cavidad_10
            if dimension.cavidad_11 is not None:
                muestras_dimensional['cavidad_11'] = dimension.cavidad_11
            if dimension.cavidad_12 is not None:
                muestras_dimensional['cavidad_12'] = dimension.cavidad_12
            if dimension.cavidad_13 is not None:
                muestras_dimensional['cavidad_13'] = dimension.cavidad_13
            if dimension.cavidad_14 is not None:
                muestras_dimensional['cavidad_14'] = dimension.cavidad_14
            if dimension.cavidad_15 is not None:
                muestras_dimensional['cavidad_15'] = dimension.cavidad_15
            if dimension.cavidad_16 is not None:
                muestras_dimensional['cavidad_16'] = dimension.cavidad_16
            if dimension.cavidad_17 is not None:
                muestras_dimensional['cavidad_17'] = dimension.cavidad_17
            if dimension.cavidad_18 is not None:
                muestras_dimensional['cavidad_18'] = dimension.cavidad_18
            if dimension.cavidad_19 is not None:
                muestras_dimensional['cavidad_19'] = dimension.cavidad_19
            if dimension.cavidad_20 is not None:
                muestras_dimensional['cavidad_20'] = dimension.cavidad_20
            if dimension.cavidad_21 is not None:
                muestras_dimensional['cavidad_21'] = dimension.cavidad_21
            if dimension.cavidad_22 is not None:
                muestras_dimensional['cavidad_22'] = dimension.cavidad_22
            if dimension.cavidad_23 is not None:
                muestras_dimensional['cavidad_23'] = dimension.cavidad_23
            if dimension.cavidad_24 is not None:
                muestras_dimensional['cavidad_24'] = dimension.cavidad_24
            if dimension.cavidad_25 is not None:
                muestras_dimensional['cavidad_25'] = dimension.cavidad_25
            if dimension.cavidad_26 is not None:
                muestras_dimensional['cavidad_26'] = dimension.cavidad_26
            if dimension.cavidad_27 is not None:
                muestras_dimensional['cavidad_27'] = dimension.cavidad_27
            if dimension.cavidad_28 is not None:
                muestras_dimensional['cavidad_28'] = dimension.cavidad_28
            if dimension.cavidad_29 is not None:
                muestras_dimensional['cavidad_29'] = dimension.cavidad_29
            if dimension.cavidad_30 is not None:
                muestras_dimensional['cavidad_30'] = dimension.cavidad_30
            if dimension.cavidad_31 is not None:
                muestras_dimensional['cavidad_31'] = dimension.cavidad_31
            if dimension.cavidad_32 is not None:
                muestras_dimensional['cavidad_32'] = dimension.cavidad_32

        pruebas = PruebasCalidad.objects.filter(id_inspeccion_p = pk)
        muestras_pruebas = {}

        for pruebas in pruebas:
            if pruebas.cavidad_1 is not None:
                muestras_pruebas['cavidad_1'] = pruebas.cavidad_1
            if pruebas.cavidad_2 is not None:
                muestras_pruebas['cavidad_2'] = pruebas.cavidad_2
            if pruebas.cavidad_3 is not None:
                muestras_pruebas['cavidad_3'] = pruebas.cavidad_3
            if pruebas.cavidad_4 is not None:
                muestras_pruebas['cavidad_4'] = pruebas.cavidad_4
            if pruebas.cavidad_5 is not None:
                muestras_pruebas['cavidad_5'] = pruebas.cavidad_5
            if pruebas.cavidad_6 is not None:
                muestras_pruebas['cavidad_6'] = pruebas.cavidad_6
            if pruebas.cavidad_7 is not None:
                muestras_pruebas['cavidad_7'] = pruebas.cavidad_7
            if pruebas.cavidad_8 is not None:
                muestras_pruebas['cavidad_8'] = pruebas.cavidad_8
            if pruebas.cavidad_9 is not None:
                muestras_pruebas['cavidad_9'] = pruebas.cavidad_9
            if pruebas.cavidad_10 is not None:
                muestras_pruebas['cavidad_10'] = pruebas.cavidad_10
            if pruebas.cavidad_11 is not None:
                muestras_pruebas['cavidad_11'] = pruebas.cavidad_11
            if pruebas.cavidad_12 is not None:
                muestras_pruebas['cavidad_12'] = pruebas.cavidad_12
            if pruebas.cavidad_13 is not None:
                muestras_pruebas['cavidad_13'] = pruebas.cavidad_13
            if pruebas.cavidad_14 is not None:
                muestras_pruebas['cavidad_14'] = pruebas.cavidad_14
            if pruebas.cavidad_15 is not None:
                muestras_pruebas['cavidad_15'] = pruebas.cavidad_15
            if pruebas.cavidad_16 is not None:
                muestras_pruebas['cavidad_16'] = pruebas.cavidad_16
            if pruebas.cavidad_17 is not None:
                muestras_pruebas['cavidad_17'] = pruebas.cavidad_17
            if pruebas.cavidad_18 is not None:
                muestras_pruebas['cavidad_18'] = pruebas.cavidad_18
            if pruebas.cavidad_19 is not None:
                muestras_pruebas['cavidad_19'] = pruebas.cavidad_19
            if pruebas.cavidad_20 is not None:
                muestras_pruebas['cavidad_20'] = pruebas.cavidad_20
            if pruebas.cavidad_21 is not None:
                muestras_pruebas['cavidad_21'] = pruebas.cavidad_21
            if pruebas.cavidad_22 is not None:
                muestras_pruebas['cavidad_22'] = pruebas.cavidad_22
            if pruebas.cavidad_23 is not None:
                muestras_pruebas['cavidad_23'] = pruebas.cavidad_23
            if pruebas.cavidad_24 is not None:
                muestras_pruebas['cavidad_24'] = pruebas.cavidad_24
            if pruebas.cavidad_25 is not None:
                muestras_pruebas['cavidad_25'] = pruebas.cavidad_25
            if pruebas.cavidad_26 is not None:
                muestras_pruebas['cavidad_26'] = pruebas.cavidad_26
            if pruebas.cavidad_27 is not None:
                muestras_pruebas['cavidad_27'] = pruebas.cavidad_27
            if pruebas.cavidad_28 is not None:
                muestras_pruebas['cavidad_28'] = pruebas.cavidad_28
            if pruebas.cavidad_29 is not None:
                muestras_pruebas['cavidad_29'] = pruebas.cavidad_29
            if pruebas.cavidad_30 is not None:
                muestras_pruebas['cavidad_30'] = pruebas.cavidad_30
            if pruebas.cavidad_31 is not None:
                muestras_pruebas['cavidad_31'] = pruebas.cavidad_31
            if pruebas.cavidad_32 is not None:
                muestras_pruebas['cavidad_32'] = pruebas.cavidad_32

        context = super().get_context_data(**kwargs)
        context['pruebas'] = PruebasCalidad.objects.filter(id_inspeccion_p = pk)
        context['inspeccionatributos'] = InspeccionAtributos.objects.filter(id_inspeccion_a = pk)
        context['inspecciondimensional'] = inspeccion_dimensional
        context['tecnicos'] = ColaboradorInspeccionCalidad.objects.filter(inspeccion = pk)
        context['materia_prima'] = Requisicion.objects.filter(numero_orden = inspeccion.numero_op)
        context['niveles'] = NivelDeInspeccion.objects.filter(inspeccion_calidad = pk)
        context['muestras_dimensional'] = muestras_dimensional
        context['muestras_pruebas'] = muestras_pruebas
        context['fecha_vencimiento'] = inspeccion.numero_op.fecha_creacion + timedelta(weeks=104)
        context['title'] = 'Detalle Inspección'
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        return context


class CertificadoCalidadView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las fichas técnicas"""

    model = CertificadosCalidad
    queryset = CertificadosCalidad.objects.all()
    context_object_name = 'CertificadosCalidad'
    permission_required = 'view_controlcalidad'

    def get_template_names(self):
        pk = self.kwargs.get('pk')
        certificado = CertificadosCalidad.objects.get(pk=pk)
        fecha_version_1 = datetime(year=2023, month=4, day=4, tzinfo=timezone(offset=timedelta()))

        if certificado.fecha_generacion < fecha_version_1:
            return 'Control_calidad/certificado_calidad_v1.html'
        return 'Control_calidad/certificado_calidad_v2.html'

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        certificado = CertificadosCalidad.objects.get(pk=pk)
        inspeccion = ControlCalidad.objects.get(id=certificado.inspeccion_certificado_id)

        context = super().get_context_data(**kwargs)
        context['controlcalidad'] = ControlCalidad.objects.get(id=certificado.inspeccion_certificado_id)
        context['pruebas'] = PruebasCalidad.objects.filter(id_inspeccion_p = inspeccion.id)
        context['inspeccionatributos'] = InspeccionAtributos.objects.filter(id_inspeccion_a = inspeccion.id)
        context['inspecciondimensional'] = InspeccionDimensional.objects.filter(id_inspeccion_d = inspeccion.id)
        context['material'] = Requisicion.objects.filter(numero_orden=inspeccion.numero_op_id)
        context['title'] = 'Certificado No. {}, Cliente: {}'.format(certificado.id, certificado.cliente_despacho)
        context['list_url'] = reverse_lazy('Control_calidad:certificados-calidad')
        context['niveles'] = NivelDeInspeccion.objects.filter(inspeccion_calidad = inspeccion.id)
        context['entity'] = 'Certificados'
        context['fecha_vencimiento'] = inspeccion.numero_op.fecha_creacion + timedelta(days=730)
        return context


class CrearInspeccionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear los productos no conformes"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = ControlCalidad
    form_class = CrearInspeccionForm
    template_name = 'Control_calidad/crear_inspeccion.html'
    success_url = reverse_lazy('ControlCalidad:Inspecciones_calidad')
    context_object_name = 'ControlCalidad'
    permission_required = 'add_controlcalidad'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    inspeccion = json.loads(request.POST['inspeccion'])
                    control = ControlCalidad()
                    control.turno = inspeccion['turno']
                    control.observaciones = inspeccion['observaciones']
                    control.numero_op_id = inspeccion['numero_op']
                    control.save(self)
                    for nivel in inspeccion['nivel']:
                        modelo_nivel = NivelDeInspeccion()
                        modelo_nivel.inspeccion_calidad_id = control.id
                        modelo_nivel.tipo_nivel = nivel['tipo_nivel']
                        modelo_nivel.codigo_nivel = nivel['codigo_nivel']
                        modelo_nivel.cantidades_inspeccionar = nivel['cantidad']
                        modelo_nivel.letra = nivel['letra']
                        modelo_nivel.save(self)
                    for colaborador in inspeccion['colaborador']:
                        modelo_colaborador = ColaboradorInspeccionCalidad()
                        modelo_colaborador.inspeccion_id = control.id
                        modelo_colaborador.colaborador_id = colaborador['id']
                        modelo_colaborador.save(self)
                    for i in inspeccion['pruebasensayos']:
                        pruebasensayos = PruebasCalidad()
                        pruebasensayos.id_inspeccion_p_id = control.id
                        pruebasensayos.pruebas_y_o_ensayos_id = i['id']
                        if 'cavidad_1' in i:
                            pruebasensayos.cavidad_1 = float(i['cavidad_1'])
                        if 'cavidad_2' in i:
                            pruebasensayos.cavidad_2 = float(i['cavidad_2'])
                        if 'cavidad_3' in i:
                            pruebasensayos.cavidad_3 = float(i['cavidad_3'])
                        if 'cavidad_4' in i:
                            pruebasensayos.cavidad_4 = float(i['cavidad_4'])
                        if 'cavidad_5' in i:
                            pruebasensayos.cavidad_5 = float(i['cavidad_5'])
                        if 'cavidad_6' in i:
                            pruebasensayos.cavidad_6 = float(i['cavidad_6'])
                        if 'cavidad_7' in i:
                            pruebasensayos.cavidad_7 = float(i['cavidad_7'])
                        if 'cavidad_8' in i:
                            pruebasensayos.cavidad_8 = float(i['cavidad_8'])
                        if 'cavidad_9' in i:
                            pruebasensayos.cavidad_9 = float(i['cavidad_9'])
                        if 'cavidad_10' in i:
                            pruebasensayos.cavidad_10 = float(i['cavidad_10'])
                        if 'cavidad_11' in i:
                            pruebasensayos.cavidad_11 = float(i['cavidad_11'])
                        if 'cavidad_12' in i:
                            pruebasensayos.cavidad_12 = float(i['cavidad_12'])
                        if 'cavidad_13' in i:
                            pruebasensayos.cavidad_13 = float(i['cavidad_13'])
                        if 'cavidad_14' in i:
                            pruebasensayos.cavidad_14 = float(i['cavidad_14'])
                        if 'cavidad_15' in i:
                            pruebasensayos.cavidad_15 = float(i['cavidad_15'])
                        if 'cavidad_16' in i:
                            pruebasensayos.cavidad_16 = float(i['cavidad_16'])
                        if 'cavidad_17' in i:
                            pruebasensayos.cavidad_17 = float(i['cavidad_17'])
                        if 'cavidad_18' in i:
                            pruebasensayos.cavidad_18 = float(i['cavidad_18'])
                        if 'cavidad_19' in i:
                            pruebasensayos.cavidad_19 = float(i['cavidad_19'])
                        if 'cavidad_20' in i:
                            pruebasensayos.cavidad_20 = float(i['cavidad_20'])
                        if 'cavidad_21' in i:
                            pruebasensayos.cavidad_21 = float(i['cavidad_21'])
                        if 'cavidad_22' in i:
                            pruebasensayos.cavidad_22 = float(i['cavidad_22'])
                        if 'cavidad_23' in i:
                            pruebasensayos.cavidad_23 = float(i['cavidad_23'])
                        if 'cavidad_24' in i:
                            pruebasensayos.cavidad_24 = float(i['cavidad_24'])
                        if 'cavidad_25' in i:
                            pruebasensayos.cavidad_25 = float(i['cavidad_25'])
                        if 'cavidad_26' in i:
                            pruebasensayos.cavidad_26 = float(i['cavidad_26'])
                        if 'cavidad_27' in i:
                            pruebasensayos.cavidad_27 = float(i['cavidad_27'])
                        if 'cavidad_28' in i:
                            pruebasensayos.cavidad_28 = float(i['cavidad_28'])
                        if 'cavidad_29' in i:
                            pruebasensayos.cavidad_29 = float(i['cavidad_29'])
                        if 'cavidad_30' in i:
                            pruebasensayos.cavidad_30 = float(i['cavidad_30'])
                        if 'cavidad_31' in i:
                            pruebasensayos.cavidad_31 = float(i['cavidad_31'])
                        if 'cavidad_32' in i:
                            pruebasensayos.cavidad_32 = float(i['cavidad_32'])
                        pruebasensayos.valor = float(i['valor_p'])
                        pruebasensayos.resultado_p = i['resultado_p']
                        pruebasensayos.save(self)
                    for i in inspeccion['inspeccionatributos']:
                        inspeccionatributos = InspeccionAtributos()
                        inspeccionatributos.id_inspeccion_a_id = control.id
                        inspeccionatributos.inspeccion_atributos_id = i['id']
                        inspeccionatributos.resultado_ia = i['resultado_ia']
                        inspeccionatributos.save(self)
                    for i in inspeccion['inspecciondimensiones']:
                        inspecciondimensional = InspeccionDimensional()
                        inspecciondimensional.id_inspeccion_d_id = control.id
                        inspecciondimensional.inspeccion_dimensional_id = i['id']
                        if 'cavidad_1' in i:
                            inspecciondimensional.cavidad_1 = float(i['cavidad_1'])
                        if 'cavidad_2' in i:
                            inspecciondimensional.cavidad_2 = float(i['cavidad_2'])
                        if 'cavidad_3' in i:
                            inspecciondimensional.cavidad_3 = float(i['cavidad_3'])
                        if 'cavidad_4' in i:
                            inspecciondimensional.cavidad_4 = float(i['cavidad_4'])
                        if 'cavidad_5' in i:
                            inspecciondimensional.cavidad_5 = float(i['cavidad_5'])
                        if 'cavidad_6' in i:
                            inspecciondimensional.cavidad_6 = float(i['cavidad_6'])
                        if 'cavidad_7' in i:
                            inspecciondimensional.cavidad_7 = float(i['cavidad_7'])
                        if 'cavidad_8' in i:
                            inspecciondimensional.cavidad_8 = float(i['cavidad_8'])
                        if 'cavidad_9' in i:
                            inspecciondimensional.cavidad_9 = float(i['cavidad_9'])
                        if 'cavidad_10' in i:
                            inspecciondimensional.cavidad_10 = float(i['cavidad_10'])
                        if 'cavidad_11' in i:
                            inspecciondimensional.cavidad_11 = float(i['cavidad_11'])
                        if 'cavidad_12' in i:
                            inspecciondimensional.cavidad_12 = float(i['cavidad_12'])
                        if 'cavidad_13' in i:
                            inspecciondimensional.cavidad_13 = float(i['cavidad_13'])
                        if 'cavidad_14' in i:
                            inspecciondimensional.cavidad_14 = float(i['cavidad_14'])
                        if 'cavidad_15' in i:
                            inspecciondimensional.cavidad_15 = float(i['cavidad_15'])
                        if 'cavidad_16' in i:
                            inspecciondimensional.cavidad_16 = float(i['cavidad_16'])
                        if 'cavidad_17' in i:
                            inspecciondimensional.cavidad_17 = float(i['cavidad_17'])
                        if 'cavidad_18' in i:
                            inspecciondimensional.cavidad_18 = float(i['cavidad_18'])
                        if 'cavidad_19' in i:
                            inspecciondimensional.cavidad_19 = float(i['cavidad_19'])
                        if 'cavidad_20' in i:
                            inspecciondimensional.cavidad_20 = float(i['cavidad_20'])
                        if 'cavidad_21' in i:
                            inspecciondimensional.cavidad_21 = float(i['cavidad_21'])
                        if 'cavidad_22' in i:
                            inspecciondimensional.cavidad_22 = float(i['cavidad_22'])
                        if 'cavidad_23' in i:
                            inspecciondimensional.cavidad_23 = float(i['cavidad_23'])
                        if 'cavidad_24' in i:
                            inspecciondimensional.cavidad_24 = float(i['cavidad_24'])
                        if 'cavidad_25' in i:
                            inspecciondimensional.cavidad_25 = float(i['cavidad_25'])
                        if 'cavidad_26' in i:
                            inspecciondimensional.cavidad_26 = float(i['cavidad_26'])
                        if 'cavidad_27' in i:
                            inspecciondimensional.cavidad_27 = float(i['cavidad_27'])
                        if 'cavidad_28' in i:
                            inspecciondimensional.cavidad_28 = float(i['cavidad_28'])
                        if 'cavidad_29' in i:
                            inspecciondimensional.cavidad_29 = float(i['cavidad_29'])
                        if 'cavidad_30' in i:
                            inspecciondimensional.cavidad_30 = float(i['cavidad_30'])
                        if 'cavidad_31' in i:
                            inspecciondimensional.cavidad_31 = float(i['cavidad_31'])
                        if 'cavidad_32' in i:
                            inspecciondimensional.cavidad_32 = float(i['cavidad_32'])
                        inspecciondimensional.promedio = i['promedio']
                        inspecciondimensional.resultado_id = i['resultado_id']
                        inspecciondimensional.save(self)
            elif action == 'search_colaborador':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                busqueda = TecnicosOperarios.objects.filter(
                    Q(nombre__icontains=request.POST['term'])|
                    Q(codigo__icontains=request.POST['term'])).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_nivel(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in NivelDeInspeccion.lista_tipo_nivel:
                produccion = Produccion.objects.get(pk=pk)
                item = {}
                item['cantidad_orden'] = produccion.cantidad_requerida
                item['tipo_nivel'] = i
                item['cantidad'] = 0
                item['letra'] = ''
                data.append(item)
        except:
            pass
        return data

    def get_pruebas(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in PruebasEnsayo.objects.filter(id_producto_p_id = Produccion.objects.get(pk=pk).producto.productos_id):
                item = i.toJSON()
                item['text'] = i.id_pruebas.variables
                item['Nombre_producto'] = i.id_producto_p.Nombre_producto
                item['version'] = i.id_producto_p.version
                data.append(item)
        except:
            pass
        return data

    def get_dimensiones(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in CaracteristicasDimensionale.objects.filter(id_producto_c_id = Produccion.objects.get(pk=pk).producto.productos_id):
                item = i.toJSON()
                item['text'] = i.id_dimensiones.caracteristicas_control
                item['Nombre_producto'] = i.id_producto_c.Nombre_producto
                item['version'] = i.id_producto_c.version
                item['resultado_id'] = '',
                item['promedio'] = 0.00
                data.append(item)
        except:
            pass
        return data

    def get_atributos(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in ControlAtributo.objects.filter(id_producto_a_id = Produccion.objects.get(pk=pk).producto.productos_id):
                item = i.toJSON()
                item['text'] = i.id_atributo.caracteristicas
                item['especificacion'] = i.id_atributo.especificacion
                item['observacion'] = i.id_atributo.observacion
                item['Nombre_producto'] = i.id_producto_a.Nombre_producto
                item['version'] = i.id_producto_a.version
                item['resultado_ia'] = '',
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        produccion = Produccion.objects.get(pk=pk)

        context['produccion'] = produccion
        context['title'] = "Nueva Inspección De Calidad"
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        context['action'] = 'add'
        context['inspeccionpruebasyoensayos'] = json.dumps(self.get_pruebas())
        context['inspecciondimensiones'] = json.dumps(self.get_dimensiones())
        context['inspeccionatributos'] = json.dumps(self.get_atributos())
        context['nivel'] = self.get_nivel()
        context['cantidad_orden'] = produccion.cantidad_requerida
        return context


class CrearCertificadoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear certificados de calidad"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = CertificadosCalidad
    form_class = CrearCertificadoForm
    template_name = 'Control_calidad/crear_certificado.html'
    success_url = reverse_lazy('ControlCalidad:certificados-calidad')
    context_object_name = 'CertificadosCalidad'
    permission_required = 'add_certificadoscalidad'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                pk = self.kwargs.get('pk')
                certificado = CertificadosCalidad()
                certificado.inspeccion_certificado_id = pk
                certificado.fecha_despacho = request.POST['fecha_despacho']
                certificado.cantidad_solicitada = request.POST['cantidad_solicitada']
                certificado.empaque_y_embalaje = request.POST['empaque_y_embalaje']
                certificado.cliente_despacho = request.POST['cliente_despacho']
                certificado.codigo_cliente = request.POST['codigo_cliente']
                certificado.observaciones = request.POST['observaciones']
                certificado.save(self)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')

        certificado = CertificadosCalidad.objects.filter(inspeccion_certificado_id = pk).aggregate(inspeccion_certificado_id= Sum('cantidad_solicitada'))
        inspeccion = ControlCalidad.objects.get(id = pk)
        produccion = Produccion.objects.get(numero_op=inspeccion.numero_op_id)
        context['produccion'] = produccion
        context['saldo'] = (produccion.cantidad_requerida - certificado['inspeccion_certificado_id']) if certificado['inspeccion_certificado_id'] is not None or 0 else produccion.cantidad_requerida
        context['title'] = "Crear certificado de la inspección: {}".format(inspeccion.id)
        context['list_url'] = reverse_lazy('Control_calidad:certificados-calidad')
        context['entity'] = 'Inspecciones'
        context['action'] = 'add'
        return context


class ListaCertificados(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para la vista de lista de controles"""

    model = CertificadosCalidad
    template_name = 'Control_calidad/lista_certificados.html'
    permission_required = 'view_certificadoscalidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in CertificadosCalidad.objects.all():
                    saldo_cliente = CertificadosCalidad.objects.filter(
                        inspeccion_certificado_id__numero_op = i.inspeccion_certificado.numero_op
                    ).aggregate(inspeccion_certificado_id=Sum('cantidad_solicitada'))
                    item = i.toJSON()
                    item['producto'] = i.inspeccion_certificado.numero_op.producto.productos.Nombre_producto
                    item['color'] = i.inspeccion_certificado.numero_op.producto.color.color
                    item['lote'] = '{}-{}'.format(i.inspeccion_certificado.numero_op_id, i.inspeccion_certificado.numero_op.fecha_creacion.year)
                    item['numero_op'] = i.inspeccion_certificado.numero_op_id
                    item['saldo'] = i.inspeccion_certificado.numero_op.cantidad_requerida - saldo_cliente['inspeccion_certificado_id'] if saldo_cliente['inspeccion_certificado_id'] is not None else i.inspeccion_certificado.numero_op.cantidad_requerida
                    item['cantidad_orden'] = i.inspeccion_certificado.numero_op.cantidad_requerida
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Certificados De Calidad'
        context['list_url'] = reverse_lazy('Control_calidad:certificados-calidad')
        context['entity'] = 'Certificados'
        return context


class InspeccionMPView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = MateriaPrimaInsumos
    form_class = CrearInspeccionMpForm
    template_name = 'Control_calidad/crear_inspeccion_mp.html'
    success_url = reverse_lazy('Inventario:Ingresos')
    context_object_name = 'MateriaPrimaInsumos'
    permission_required = 'add_materiaprimainsumos'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                pk = kwargs.get('pk')
                info_lote = Entrada.objects.get(pk=pk)
                with transaction.atomic():
                    inspeccion = json.loads(request.POST['inspeccion'])
                    print(request.POST['inspeccion'])
                    insp_materia_prima = MateriaPrimaInsumos()
                    insp_materia_prima.materia_prima_insumo_id = info_lote.id
                    insp_materia_prima.arte_cliente = inspeccion['arte_cliente']
                    insp_materia_prima.unidades_muestra = inspeccion['unidades_muestra']
                    insp_materia_prima.unidades_lote = info_lote.cantidad_ingresada
                    insp_materia_prima.proveedor = inspeccion['proveedor']
                    insp_materia_prima.fecha_lote = info_lote.fecha_ingreso
                    insp_materia_prima.arte_ingreso = inspeccion['arte_ingreso']
                    insp_materia_prima.unidades_empaque = inspeccion['unidades_empaque']
                    insp_materia_prima.certificado = True if inspeccion['certificado'] == 'Cumple' else False
                    insp_materia_prima.especificaciones = True if inspeccion['especificaciones'] == 'Cumple' else False
                    insp_materia_prima.lote = info_lote.lote
                    insp_materia_prima.lote_ingreso = True if inspeccion['lote_ingreso'] == 'Si' else False
                    insp_materia_prima.observaciones = inspeccion['observaciones']
                    insp_materia_prima.revisado_por = inspeccion['revisado_por']
                    insp_materia_prima.aprobado = True if inspeccion['aprobado'] == 'Si' else False
                    insp_materia_prima.tolerado = True if inspeccion['tolerado'] == 'Si' else False
                    insp_materia_prima.estado = inspeccion['estado']
                    insp_materia_prima.save(self)
                    for especificacion in inspeccion['analisis']:
                        analisis = Analisis()
                        analisis.inspeccion_id = insp_materia_prima.id
                        analisis.especificacion = especificacion['especificacion']
                        analisis.cumple = especificacion['cumple']
                        analisis.save(self)
                    for dimension in inspeccion['dimensional']:
                        dimensional = Dimensional()
                        dimensional.inspeccion_id = insp_materia_prima.id
                        dimensional.especificacion = dimension['especificacion']
                        if 'muestra_1' in dimension:
                            dimensional.muestra_1 = dimension['muestra_1']
                        if 'muestra_2' in dimension:
                            dimensional.muestra_2 = dimension['muestra_2']
                        if 'muestra_3' in dimension:
                            dimensional.muestra_3 = dimension['muestra_3']
                        if 'muestra_4' in dimension:
                            dimensional.muestra_4 = dimension['muestra_4']
                        if 'muestra_5' in dimension:
                            dimensional.muestra_5 = dimension['muestra_5']
                        if 'muestra_6' in dimension:
                            dimensional.muestra_6 = dimension['muestra_6']
                        if 'muestra_7' in dimension:
                            dimensional.muestra_7 = dimension['muestra_7']
                        if 'muestra_8' in dimension:
                            dimensional.muestra_8 = dimension['muestra_8']
                        if 'muestra_9' in dimension:
                            dimensional.muestra_9 = dimension['muestra_9']
                        if 'muestra_10' in dimension:
                            dimensional.muestra_10 = dimension['muestra_10']
                        if 'muestra_11' in dimension:
                            dimensional.muestra_11 = dimension['muestra_11']
                        if 'muestra_12' in dimension:
                            dimensional.muestra_12 = dimension['muestra_12']
                        if 'muestra_13' in dimension:
                            dimensional.muestra_13 = dimension['muestra_13']
                        dimensional.cumple = dimension['cumple']
                        dimensional.save(self)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_especificaiones_analisis(self):
        data = []
        try:
            for i in Analisis.especificacion_list:
                item = {}
                item['especificacion'] = i
                data.append(item)
        except:
            pass
        return data

    def get_especificaiones_dimensiones(self):
        data = []
        try:
            for i in Dimensional.especificacion_list:
                item = {}
                item['especificacion'] = i
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        ingreso = Entrada.objects.get(pk=pk)

        context['Entrada'] = ingreso
        context['title'] = "Inspección"
        context['list_url'] = reverse_lazy('Inventario:Ingresos')
        context['analisis'] = json.dumps(self.get_especificaiones_analisis())
        context['dimensional'] = json.dumps(self.get_especificaiones_dimensiones())
        context['entity'] = 'Inspecciones'
        context['action'] = 'add'
        return context


class DetalleInspeccionMpView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):

    model = MateriaPrimaInsumos
    template_name = 'Control_calidad/detalle_inspeccion.html'
    context_object_name = 'MateriaPrimaInsumos'
    permission_required = 'view_materiaprimainsumos'

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        materia_prima = MateriaPrimaInsumos.objects.get(pk=pk)
        dimensional = Dimensional.objects.filter(inspeccion_id = materia_prima.id)
        muestras = {}

        for muestra in dimensional:
            if muestra.muestra_1 is not None:
                muestras['muestra_1'] = muestra.muestra_1
            if muestra.muestra_2 is not None:
                muestras['muestra_2'] = muestra.muestra_2
            if muestra.muestra_3 is not None:
                muestras['muestra_3'] = muestra.muestra_3
            if muestra.muestra_4 is not None:
                muestras['muestra_4'] = muestra.muestra_4
            if muestra.muestra_5 is not None:
                muestras['muestra_5'] = muestra.muestra_5
            if muestra.muestra_6 is not None:
                muestras['muestra_6'] = muestra.muestra_6
            if muestra.muestra_7 is not None:
                muestras['muestra_7'] = muestra.muestra_7
            if muestra.muestra_8 is not None:
                muestras['muestra_8'] = muestra.muestra_8
            if muestra.muestra_9 is not None:
                muestras['muestra_9'] = muestra.muestra_9
            if muestra.muestra_10 is not None:
                muestras['muestra_10'] = muestra.muestra_10
            if muestra.muestra_11 is not None:
                muestras['muestra_11'] = muestra.muestra_11
            if muestra.muestra_12 is not None:
                muestras['muestra_12'] = muestra.muestra_12
            if muestra.muestra_13 is not None:
                muestras['muestra_13'] = muestra.muestra_13

        context = super().get_context_data(**kwargs)
        context['analisis'] = Analisis.objects.filter(inspeccion_id = materia_prima.id)
        context['dimensional'] = dimensional
        context['entrada'] = Entrada.objects.get(id = materia_prima.materia_prima_insumo_id)
        context['muestras'] = muestras
        context['title'] = 'Detalle inspección. {}, producto: {}, referencia {}'.format(
            materia_prima.id, 
            materia_prima.materia_prima_insumo.ingreso_materia_prima.nombre,
            materia_prima.materia_prima_insumo.ingreso_materia_prima.referencia
            )
        context['list_url'] = reverse_lazy('Inventario:Ingresos')
        context['entity'] = 'Inspección Mp'
        return context


class ActualizarInspeccionMPView(LoginRequiredMixin, UpdateView):

    template_name = 'Control_calidad/actualizar_inspecion_mp.html'
    model = MateriaPrimaInsumos
    success_url = reverse_lazy('Inventario:Ingresos')
    form_class = ActualizarInspeccionMpForm
    context_object_name = 'MateriaPrimaInsumos'

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
        context['title'] = 'Actualizar Inspeccion: '
        context['list_url'] = reverse_lazy('Inventario:Ingresos')
        context['entity'] = 'Inspecciones'
        context['action'] = 'edit'
        return context


class HistoricoInspeccionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, TemplateView):
    model = ControlCalidad
    template_name = 'Control_calidad/historico_inspecciones.html'
    context_object_name = 'control_calidad'
    permission_required = 'view_controlcalidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                producto = request.POST['producto']
                if producto == '':
                    data = []
                    calidad_query = ControlCalidad.objects.none()
                    for i in calidad_query:
                        colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id)
                        item = i.toJSON()
                        item['producto'] = i.numero_op.producto.productos.Nombre_producto
                        item['cliente'] = i.numero_op.cliente
                        item['maquina'] = i.numero_op.maquina
                        item['lote'] = '{}-{}'.format(i.numero_op_id, i.numero_op.fecha_creacion.year)
                        item['fecha_creacion'] = i.fecha_creacion
                        item['inspector'] = i.inspector.get_full_name()
                        item['colaboradores'] = [{'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                        item['pnc'] = ProductoNoConforme.objects.filter(id_inspeccion=i.id).count()
                        data.append(item)
                elif producto != '':
                    data = []
                    calidad_query = ControlCalidad.objects.filter(
                        numero_op__producto__productos__Nombre_producto__icontains=producto
                    )
                    for i in calidad_query:
                        colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id)
                        item = i.toJSON()
                        item['producto'] = i.numero_op.producto.productos.Nombre_producto
                        item['cliente'] = i.numero_op.cliente
                        item['maquina'] = i.numero_op.maquina
                        item['lote'] = '{}-{}'.format(i.numero_op_id, i.numero_op.fecha_creacion.year)
                        item['fecha_creacion'] = i.fecha_creacion
                        item['inspector'] = i.inspector.get_full_name()
                        item['colaboradores'] = [{'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                        item['pnc'] = ProductoNoConforme.objects.filter(id_inspeccion=i.id).count()
                        data.append(item)
            elif action == 'search_details_pnc':
                data = []
                for pnc in TrazabilidadProductoNoConforme.objects.filter(id_inspeccion = request.POST['id_inspeccion']):
                    item = pnc.toJSON()
                    item['numero_op'] = pnc.id_inspeccion.numero_op_id
                    item['inspector'] = pnc.inspector_calidad.get_full_name()
                    item['turno'] = pnc.id_inspeccion.turno
                    item['tipo_pnc'] = pnc.tipo_pnc.motivo
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historico Inspecciones'
        context['list_url'] = reverse_lazy('Historico')
        context['entity'] = 'Historico'
        context['form'] = HistoricalForm()
        return context
