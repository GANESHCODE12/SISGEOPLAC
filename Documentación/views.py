"""Vistas de la aplicación de sistema documental"""

#Django
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#Form
from Documentación.forms import *

#mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

#Models
from Documentación.models import *



class DocumentosView(LoginRequiredMixin,ValidatePermissionRequiredMixin, ListView):
    """Vista de listado de documentos"""

    template_name = 'Documentacion/lista_documentos.html'
    model = Documentacion
    permission_required = 'view_documentacion'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Documentacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado maestro de documentos'
        context['list_url'] = reverse_lazy('Documentación:Documentos')
        context['entity'] = 'Documentos'
        return context


class CrearDocumentoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las ordenes de producción"""

    template_name = 'Documentacion/crear_documento.html'
    form_class = CrearDocumentoForm
    success_url = reverse_lazy('Documentación:Documentos')
    permission_required = 'add_documentacion'

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
        context['title'] = 'Nuevo Documento'
        context['list_url'] = reverse_lazy('Documentación:Documentos')
        context['entity'] = 'Documentos'
        context['action'] = 'add'
        return context


class DetalleDocumentoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las ordenes"""

    template_name = 'Documentacion/detalle_documento.html'
    queryset = Documentacion.objects.all()
    context_object_name = 'Documentacion'
    permission_required = 'view_documentacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Documento'
        context['list_url'] = reverse_lazy('Documentación:Documentos')
        context['entity'] = 'Documentos'
        return context


class ActualizarDocumento(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    """Vista para actualización de los documentos"""
    
    model = Documentacion
    template_name = 'Documentacion/actualizar_documento.html'
    form_class = ActualizarDocumentoForm
    success_url = reverse_lazy('Documentación:Documentos')
    context_object_name = 'Documentacion'
    permission_required = 'change_documentacion'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

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
        context['title'] = 'Actualizar Documento'
        context['list_url'] = reverse_lazy('Documentación:Documentos')
        context['entity'] = 'Documentos'
        context['action'] = 'edit'
        return context