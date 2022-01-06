"""Vistas de la aplicación Producto no conforme"""

#Django
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#Form
from PNC.forms import ActualizarPNC, CrearPncForm

#Models
from PNC.models import ProductoNoConforme
from Control_calidad.models import ControlCalidad


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
                    item = i.toJSON()
                    item['numero_op'] = i.id_inspeccion.numero_op_id
                    item['inspector'] = i.inspector_calidad.get_full_name()
                    item['tecnico'] = i.id_inspeccion.tecnico
                    item['operario'] = i.id_inspeccion.operario
                    item['turno'] = i.id_inspeccion.turno
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

    def form_valid(self, form):
        """Acciones cuando el formulario es valido"""

        instance_ProductoNoConforme = form.save(commit=False)
        instance_ProductoNoConforme.id_inspeccion = self.instance_ControlCalidad
        instance_ProductoNoConforme.save()

        return super(NuevoPncView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        """Función para obtener el valor de los modelos
        de producción y control producción y extenderlo 
        al contexto de pnc"""
            
        self.instance_ControlCalidad = get_object_or_404(ControlCalidad, pk=kwargs.get('pk'))
        return super(NuevoPncView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Función para públicar los datos escritos"""

        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                self.instance_ControlCalidad = get_object_or_404(ControlCalidad, pk=kwargs.get('pk'))
                super(NuevoPncView,self).post(request, *args, **kwargs)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        """Función que agrega al contexto la información 
        de producción y control producción"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['control_calidad'] = ControlCalidad.objects.get(pk=pk)
        context['pnc'] = ProductoNoConforme.objects.all().filter(id_inspeccion = pk)
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
        context = super().get_context_data(**kwargs)
        context['control_calidad'] = ControlCalidad.objects.get(pk=pk)
        context['title'] = 'Detalle PNC'
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        return context


class ActualizarPNC(LoginRequiredMixin, UpdateView):
    """Vista para actualizar estado y observaciones de PNC"""

    template_name = 'PNC/actualizar_pnc.html'
    model = ProductoNoConforme
    success_url = reverse_lazy('PNC:Productos_no_conformes')
    form_class = ActualizarPNC
    context_object_name = 'ProductoNoConforme'

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
        context['title'] = 'Actualizar PNC'
        context['list_url'] = reverse_lazy('PNC:Productos_no_conformes')
        context['entity'] = 'Lista PNC'
        context['action'] = 'edit'
        return context
