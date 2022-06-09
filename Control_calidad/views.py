"""Vistas de la aplicación Inspecciones de calidad"""

#Django
from django.http.response import JsonResponse
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
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


#Utilidades
import json


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
                for i in ControlCalidad.objects.all():
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.Nombre_producto
                    item['cliente'] = i.numero_op.cliente
                    item['maquina'] = i.numero_op.maquina
                    item['lote'] = i.numero_op.lote
                    item['fecha_creacion'] = i.fecha_creacion
                    item['inspector'] = i.inspector.get_full_name()
                    item['saldo'] = i.numero_op.cantidad_requerida - i.cantidad_solicitada
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
        context = super().get_context_data(**kwargs)
        context['pruebas'] = PruebasCalidad.objects.all().filter(id_inspeccion_p = pk)
        context['inspeccionatributos'] = InspeccionAtributos.objects.all().filter(id_inspeccion_a = pk)
        context['inspecciondimensional'] = InspeccionDimensional.objects.all().filter(id_inspeccion_d = pk)
        context['title'] = 'Detalle Inspección'
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        return context


class ActualizarCertificado(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    """Vista para actualización de los certificados"""
    
    template_name = 'Control_calidad/actualizar_certificado.html'
    model = ControlCalidad
    form_class = ActualizarInspeccionForm
    success_url = reverse_lazy('Control_calidad:Inspecciones_calidad')
    context_object_name = 'ControlCalidad'
    permission_required = 'change_controlcalidad'
    

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
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        pk1 = ControlCalidad.objects.get(id=pk).numero_op_id

        produccion = Produccion.objects.get(numero_op=pk1)
        inspeccion = ControlCalidad.objects.all().filter(numero_op_id= pk1).aggregate(numero_op_id= Sum('cantidad_solicitada'))

        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Certificado'
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        context['saldo'] = (produccion.cantidad_requerida - inspeccion['numero_op_id']) if inspeccion['numero_op_id'] is not None or 0 else produccion.cantidad_requerida
        context['action'] = 'edit'
        return context


class CertificadoCalidad(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las fichas técnicas"""

    model = ControlCalidad
    template_name = 'Control_calidad/certificado_calidad.html'
    queryset = ControlCalidad.objects.all()
    context_object_name = 'ControlCalidad'
    permission_required = 'view_controlcalidad'

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['controlcalidad'] = ControlCalidad.objects.get(pk=pk)
        context['pruebas'] = PruebasCalidad.objects.all().filter(id_inspeccion_p = pk)
        context['inspeccionatributos'] = InspeccionAtributos.objects.all().filter(id_inspeccion_a = pk)
        context['inspecciondimensional'] = InspeccionDimensional.objects.all().filter(id_inspeccion_d = pk)
        context['title'] = 'Actualizar inspección'
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
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
                    control.tecnico = inspeccion['tecnico']
                    control.operario = inspeccion['operario']
                    control.turno = inspeccion['turno']
                    control.fecha_despacho = inspeccion['fecha_despacho']
                    control.cantidad_solicitada = inspeccion['cantidad_solicitada']
                    control.empaque_y_embalaje = inspeccion['empaque_y_embalaje']
                    control.observaciones = inspeccion['observaciones']
                    control.numero_op_id = inspeccion['numero_op']
                    control.save(self)

                    for i in inspeccion['pruebasensayos']:
                        pruebasensayos = PruebasCalidad()
                        pruebasensayos.id_inspeccion_p_id = control.id
                        pruebasensayos.pruebas_y_o_ensayos_id = i['id']
                        pruebasensayos.metodo_p = i['metodo_p']
                        pruebasensayos.resultado_p = i['resultado_p']
                        pruebasensayos.valor = float(i['valor'])
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
                        inspecciondimensional.promedio = i['promedio']
                        inspecciondimensional.resultado_id = i['resultado_id']
                        inspecciondimensional.save(self)

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_pruebas(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in PruebasEnsayo.objects.filter(id_producto_p_id = Produccion.objects.get(pk=pk).producto_id):
                item = i.toJSON()
                item['text'] = i.id_pruebas.variables
                item['Nombre_producto'] = i.id_producto_p.Nombre_producto
                item['version'] = i.id_producto_p.version
                item['metodo_p'] = '',
                item['resultado_p'] = '',
                data.append(item)
        except:
            pass
        return data

    def get_dimensiones(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in CaracteristicasDimensionale.objects.filter(id_producto_c_id = Produccion.objects.get(pk=pk).producto_id):
                item = i.toJSON()
                item['text'] = i.id_dimensiones.caracteristicas_control
                item['Nombre_producto'] = i.id_producto_c.Nombre_producto
                item['version'] = i.id_producto_c.version
                item['resultado_id'] = '',
                data.append(item)
        except:
            pass
        return data

    def get_atributos(self):
        data = []
        try:
            pk = self.kwargs.get('pk')
            for i in ControlAtributo.objects.filter(id_producto_a_id = Produccion.objects.get(pk=pk).producto_id):
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
        inspeccion = ControlCalidad.objects.all().filter(numero_op_id= pk).aggregate(numero_op_id= Sum('cantidad_solicitada'))

        context['produccion'] = Produccion.objects.get(pk=pk)
        context['title'] = "Nueva Inspección De Calidad"
        context['list_url'] = reverse_lazy('Control_calidad:Inspecciones_calidad')
        context['entity'] = 'Inspecciones'
        context['action'] = 'add'
        context['saldo'] = (produccion.cantidad_requerida - inspeccion['numero_op_id']) if inspeccion['numero_op_id'] is not None else produccion.cantidad_requerida
        context['inspeccionpruebasyoensayos'] = json.dumps(self.get_pruebas())
        context['inspecciondimensiones'] = json.dumps(self.get_dimensiones())
        context['inspeccionatributos'] = json.dumps(self.get_atributos())
        return context
