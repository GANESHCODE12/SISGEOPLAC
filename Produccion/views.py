"""Vistas de la aplicación de producción"""

#Django
from tokenize import group
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

#Form
from Produccion.forms import *

#Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# load model
from swapper import load_model

#Utils
from Plasmotec import utils
import threading
import json
from datetime import date

#Models
from Produccion.models import *
from Productos.models import Productos_colores
from Control_calidad.models import *
from Control_produccion.models import *
from PNC.models import *
from Inventario.models import Requisicion


class ListaOrdenesView(LoginRequiredMixin, ListView):

    template_name = 'Produccion/lista_ordenes.html'
    model = Produccion

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
                data = []
                produccion_query = Produccion.objects.all().iterator()
                for i in produccion_query:
                    saldo_a =ControlProduccion.objects.all(
                    ).filter(numero_op_id = i.numero_op
                    ).aggregate(numero_op_id=Sum('cantidad_producida'))

                    saldo_cliente_a = CertificadosCalidad.objects.all(
                    ).filter(inspeccion_certificado_id__numero_op = i.numero_op
                    ).aggregate(inspeccion_certificado_id=Sum('cantidad_solicitada'))

                    item = i.toJSON()
                    item['Nombre_producto'] = i.producto.productos.Nombre_producto
                    item['saldo_a'] = saldo_a['numero_op_id'] if saldo_a['numero_op_id'] is not None else 0
                    item['saldo'] = (i.cantidad_requerida - saldo_a['numero_op_id']) if saldo_a['numero_op_id'] is not None else i.cantidad_requerida
                    item['saldo_cliente'] = (i.cantidad_requerida - saldo_cliente_a['inspeccion_certificado_id']) if saldo_cliente_a['inspeccion_certificado_id'] is not None else i.cantidad_requerida
                    item['color'] = i.producto.color.color
                    item['lote'] = '{}-{}'.format(i.numero_op, i.fecha_creacion.year)
                    data.append(item)
            elif action == 'search_details_controls':
                data = []
                control = ControlProduccion.objects.filter(numero_op_id = request.POST['numero_op']).iterator() 
                for i in control:
                    colaboradores = ColaboradorControlProduccion.objects.filter(control_id=i.id).iterator()
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.productos.Nombre_producto
                    item['fecha'] = i.fecha_creacion.strftime('%d/%m/%Y')
                    item['orden'] = i.numero_op_id
                    item['maquina'] = i.numero_op.maquina
                    item['colaboradores'] = [{'nombre': colaborador.colaborador.nombre} for colaborador in colaboradores]
                    data.append(item)
            elif action == 'search_details_MPI':
                data = []
                requisicion_query = Requisicion.objects.filter(numero_orden_id = request.POST['numero_op'])
                requisicion = requisicion_query.iterator()
                for i in requisicion:
                    item = i.toJSON()
                    item['producto'] = i.material_solicitado.ingreso_materia_prima.nombre
                    item['categoria'] = i.material_solicitado.ingreso_materia_prima.categoria
                    item['referencia'] = i.material_solicitado.ingreso_materia_prima.referencia
                    item['proveedor'] = i.material_solicitado.ingreso_materia_prima.proveedor
                    item['ingresado'] = i.material_solicitado.ingresado_por.get_full_name()
                    item['medida'] = i.material_solicitado.ingreso_materia_prima.Unidad_Meidida
                    item['fecha'] = i.material_solicitado.fecha_ingreso.strftime('%d/%m/%Y')
                    item['lote'] = i.material_solicitado.lote
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ordenes de Producción'
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        return context


class CrearOrdenView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    form_class = CrearForm
    template_name = 'Produccion/crear_orden.html'
    success_url = reverse_lazy('Produccion:Ordenes_produccion')
    permission_required = 'add_produccion'

    def form_valid(self, form):

        instance_Produccion = form.save(commit=False)
        instance_Produccion.producto = self.instance_Producto
        instance_Produccion.save()

        return super(CrearOrdenView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
            
        self.instance_Producto = get_object_or_404(Productos_colores, pk=kwargs.get('pk'))
        return super(CrearOrdenView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Producto = get_object_or_404(Productos_colores, pk=kwargs.get('pk'))
                super(CrearOrdenView,self).post(request, *args, **kwargs)

                producto = Productos_colores.objects.get(id=kwargs.get('pk'))
                orden = Produccion.objects.last()

                groups = Group.objects.get(name="Ordenes producción")
                users_groups = groups.user_set.all()

                usuarios = [usuario.email for usuario in users_groups]

                threading_emails = threading.Thread(target=utils.send_email,
                    args=(
                    'confidencial@plasmotecsas.com',
                    usuarios,
                    'Plasmotec - Se ha creado la orden {} con el producto {} {}'.format(
                        self.object, 
                        producto.productos.Nombre_producto,
                        producto.color.color
                    ),
                    'order',
                    {
                        "producto": '{} {}'.format(producto.productos.Nombre_producto, producto.color.color),
                        "orden": self.object,
                        "lote": '{}-{}'.format(orden.numero_op + 1, date.today().year),
                        "orden_compra": request.POST['orden_compra'],
                        "cliente": request.POST['cliente'],
                        "cantidad_requerida": request.POST['cantidad_requerida'],
                        "maquina": request.POST['maquina'],
                        "estado_op": request.POST['estado_op'],
                        "fecha_entrega": request.POST['fecha_entrega'],
                        "observaciones": request.POST['observaciones'],
                    },
                ))

                threading_emails.start()
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['producto'] = Productos_colores.objects.get(pk=pk)
        context['title'] = 'Nueva Orden de Producción'
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        context['action'] = 'add'
        return context 


class DetalleOrdenView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):

    template_name = 'Produccion/detalle_orden.html'
    queryset = Produccion.objects.all()
    context_object_name = 'Produccion'
    permission_required = 'view_produccion'

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')
        produccion = Produccion.objects.get(numero_op=pk)
        context = super().get_context_data(**kwargs)
        context['materia_prima'] = Requisicion.objects.all().filter(numero_orden=pk, material_solicitado__ingreso_materia_prima__categoria="Materia Prima").last()
        context['pigmento'] = Requisicion.objects.all().filter(numero_orden=pk, material_solicitado__ingreso_materia_prima__categoria="Pigmento").last()
        context['title'] = 'Detalle Orden'
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        context['action'] = 'add'
        context['anio'] = produccion.fecha_creacion.year
        return context


class ActualizarOrdenNotificacionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    
    template_name = 'Produccion/actualizar_orden.html'
    model = Produccion
    success_url = reverse_lazy('Produccion:Ordenes_produccion')
    form_class = ActuaizarOrden
    context_object_name = 'Produccion'
    permission_required = 'change_produccion'

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
                
                notificacion_id = self.kwargs.get('Notificacion_id')
                Notify = load_model('notify', 'Notification')

                notificacion = Notify.objects.get(id=notificacion_id)
                notificacion.read = True
                notificacion.save()

                producto = Productos_colores.objects.get(id=self.object.producto.id)
                orden = Produccion.objects.last()

                groups = Group.objects.get(name="Ordenes producción")
                users_groups = groups.user_set.all()

                usuarios = [usuario.email for usuario in users_groups]

                threading_emails = threading.Thread(target=utils.send_email,
                    args=(
                    'confidencial@plasmotecsas.com',
                    usuarios,
                    'Plasmotec - Se ha modificado la orden {} con el producto {} {}'.format(
                        self.object, 
                        producto.productos.Nombre_producto,
                        producto.color.color
                    ),
                    'order_update',
                    {
                        "producto": '{} {}'.format(producto.productos.Nombre_producto, producto.color.color),
                        "orden": self.object,
                        "lote": '{}-{}'.format(orden.numero_op + 1, date.today().year),
                        "cantidad_requerida": request.POST['cantidad_requerida'],
                        "maquina": request.POST['maquina'],
                        "estado_op": request.POST['estado_op'],
                        "fecha_entrega": request.POST['fecha_entrega'],
                        "observaciones": request.POST['observaciones'],
                        "materia_prima_adicional": request.POST['materia_prima_adicional'],
                        "pigmento_adicional": request.POST['pigmento_adicional'],
                        "aprobacion_orden": request.POST['aprobacion_orden'] if 'aprobacion_orden' in request.POST else '',
                        "aprobacion_materia_prima": request.POST['aprobacion_materia_prima'] if 'aprobacion_materia_prima' in request.POST else '',
                        "aprobacion_pigmento": request.POST['aprobacion_pigmento'] if 'aprobacion_pigmento' in request.POST else '',

                    },
                ))

                threading_emails.start()

            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Orden: '
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        context['action'] = 'edit'
        return context


class ActualizarOrdenView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    
    template_name = 'Produccion/actualizar_orden.html'
    model = Produccion
    success_url = reverse_lazy('Produccion:Ordenes_produccion')
    form_class = ActuaizarOrden
    context_object_name = 'Produccion'
    permission_required = 'change_produccion'

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
                
                producto = Productos_colores.objects.get(id=self.object.producto.id)
                orden = Produccion.objects.last()

                groups = Group.objects.get(name="Ordenes producción")
                users_groups = groups.user_set.all()

                usuarios = [usuario.email for usuario in users_groups]

                threading_emails = threading.Thread(target=utils.send_email,
                    args=(
                    'confidencial@plasmotecsas.com',
                    usuarios,
                    'Plasmotec - Se ha modificado la orden {} con el producto {} {}'.format(
                        self.object, 
                        producto.productos.Nombre_producto,
                        producto.color.color
                    ),
                    'order_update',
                    {
                        "producto": '{} {}'.format(producto.productos.Nombre_producto, producto.color.color),
                        "orden": self.object,
                        "lote": '{}-{}'.format(orden.numero_op + 1, date.today().year),
                        "cantidad_requerida": request.POST['cantidad_requerida'],
                        "maquina": request.POST['maquina'],
                        "estado_op": request.POST['estado_op'],
                        "fecha_entrega": request.POST['fecha_entrega'],
                        "observaciones": request.POST['observaciones'],
                        "materia_prima_adicional": request.POST['materia_prima_adicional'],
                        "pigmento_adicional": request.POST['pigmento_adicional'],
                        "aprobacion_orden": request.POST['aprobacion_orden'] if 'aprobacion_orden' in request.POST else '',
                        "aprobacion_materia_prima": request.POST['aprobacion_materia_prima'] if 'aprobacion_materia_prima' in request.POST else '',
                        "aprobacion_pigmento": request.POST['aprobacion_pigmento'] if 'aprobacion_pigmento' in request.POST else '',

                    },
                ))

                threading_emails.start()

            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Orden: '
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        context['action'] = 'edit'
        return context


class CrearDesarrolloView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    form_class = CrearDesarrolloForm
    template_name = 'Produccion/crear_desarrollo.html'
    success_url = reverse_lazy('Produccion:Ordenes_produccion')
    permission_required = 'add_desarrollo'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                desarrollo_post = json.loads(request.POST['desarrollo'])
                print(request.POST['desarrollo'])
                desarrollo = Desarrollo()
                desarrollo.producto = desarrollo_post['producto']
                desarrollo.ciclo = desarrollo_post['ciclo']
                desarrollo.solicitado_por = desarrollo_post['solicitado_por']
                desarrollo.fecha_limite_entrega = desarrollo_post['fecha_limite_entrega']
                desarrollo.cantidad = desarrollo_post['cantidad']
                desarrollo.tipo_empaque = desarrollo_post['tipo_empaque']
                desarrollo.maquina = desarrollo_post['maquina']
                desarrollo.objetivo_muestra = desarrollo_post['objetivo_muestra']
                desarrollo.molde_nuevo = desarrollo_post['molde_nuevo']
                desarrollo.es_funcional = desarrollo_post['es_funcional']
                desarrollo.diseño = desarrollo_post['diseño']
                desarrollo.variables = desarrollo_post['variables']
                desarrollo.peso_solicitado = desarrollo_post['peso_solicitado']
                desarrollo.observaciones = desarrollo_post['observaciones']
                desarrollo.color = desarrollo_post['color']
                desarrollo.muestras = desarrollo_post['muestras']
                desarrollo.autorizacion = desarrollo_post['autorizacion']
                desarrollo.save(self)
                for produccion in desarrollo_post['produccion']:
                    modelo_produccion = DesarrolloMuestras()
                    modelo_produccion.desarrollo_id = desarrollo.id
                    modelo_produccion.mp = produccion['mp']
                    modelo_produccion.pigmentos = produccion['pigmentos']
                    modelo_produccion.empaque = produccion['empaque']
                    modelo_produccion.maquila = produccion['maquila']
                    modelo_produccion.operario = produccion['operario']
                    modelo_produccion.tecnico = produccion['tecnico']
                    modelo_produccion.montaje = produccion['montaje']
                    modelo_produccion.total = produccion['suma_total']
                    modelo_produccion.save(self)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_especificaiones_analisis(self):
        data = []
        try:
            for i in DesarrolloMuestras.lista_especificaciones:
                item = {}
                item['especificacion'] = i
                data.append(item)
        except:
            pass
        return data

                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produccion'] = json.dumps(self.get_especificaiones_analisis())
        context['title'] = 'Nuevo desarrollo'
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Desarrollo'
        context['action'] = 'add'
        return context 
