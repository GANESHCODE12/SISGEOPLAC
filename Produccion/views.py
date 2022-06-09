"""Vistas de la aplicación de producción"""

#Django
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

#Models
from Produccion.models import *
from Productos.models import Producto
from Control_calidad.models import *
from Control_produccion.models import *
from PNC.models import *


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
                for i in Produccion.objects.all():
                    saldo_a =ControlProduccion.objects.all(
                    ).filter(numero_op_id = i.numero_op
                    ).aggregate(numero_op_id=Sum('cantidad_producida'))

                    saldo_cliente_a =ControlCalidad.objects.all(
                    ).filter(numero_op_id = i.numero_op
                    ).aggregate(numero_op_id=Sum('cantidad_solicitada'))

                    item = i.toJSON()
                    item['Nombre_producto'] = i.producto.Nombre_producto
                    item['saldo'] = (i.cantidad_requerida - saldo_a['numero_op_id']) if saldo_a['numero_op_id'] is not None else i.cantidad_requerida
                    item['saldo_cliente'] = (i.cantidad_requerida - saldo_cliente_a['numero_op_id']) if saldo_cliente_a['numero_op_id'] is not None else i.cantidad_requerida
                    item['color'] = i.color
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
            
        self.instance_Producto = get_object_or_404(Producto, pk=kwargs.get('pk'))
        return super(CrearOrdenView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Producto = get_object_or_404(Producto, pk=kwargs.get('pk'))
                super(CrearOrdenView,self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['producto'] = Producto.objects.get(pk=pk)
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
        context = super().get_context_data(**kwargs)
        context['produccion'] = Produccion.objects.all().filter(producto = pk)
        context['title'] = 'Detalle Orden'
        context['list_url'] = reverse_lazy('Produccion:Ordenes_produccion')
        context['entity'] = 'Ordenes'
        context['action'] = 'add'
        return context


class ActualizarOrden(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    
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