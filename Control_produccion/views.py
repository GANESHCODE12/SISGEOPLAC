"""Vistas de la aplicación control de producción"""

#Django
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

#Form
from Control_produccion.forms import *

#Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

#Models
from Control_produccion.models import *
from Produccion.models import Produccion


class ListaControl(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Control_produccion/lista_controles.html'
    model = ControlProduccion
    permission_required = 'view_controlproduccion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ControlProduccion.objects.all():
                    item = i.toJSON()
                    item['producto'] = i.numero_op.producto.Nombre_producto
                    item['supervisor'] = i.supervisor.get_full_name()
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


class CrearNuevoControlView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):

    template_name = 'Control_produccion/crear_control.html'
    form_class = CrearControlForm
    success_url = reverse_lazy('Control_produccion:Control_orden')
    context_object_name = 'Control_produccion'
    permission_required = 'add_controlproduccion'

    def form_valid(self, form):

        instance_Control_produccion = form.save(commit=False)
        instance_Control_produccion.numero_op = self.instance_Produccion
        instance_Control_produccion.save()

        return super(CrearNuevoControlView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
            
        self.instance_Produccion = get_object_or_404(Produccion, pk=kwargs.get('pk'))
        return super(CrearNuevoControlView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_Produccion = get_object_or_404(Produccion, pk=kwargs.get('pk'))
                super(CrearNuevoControlView,self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        """Función que agrega el contexto de la información 
        de producción"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['produccion'] = Produccion.objects.get(pk=pk)
        context['title'] = "Nuevo Control"
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Controles'
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
        context['title'] = 'Detalle control'
        context['list_url'] = reverse_lazy('Control_produccion:Control_orden')
        context['entity'] = 'Controles'
        return context