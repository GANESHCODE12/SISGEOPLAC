"""Vistas de la aplicación Producto no conforme"""

#Django
from django.views.generic.base import TemplateView
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#Models
from users.models import User
from Productos.models import Producto

#Formularios
from Plasmotec.forms import TestForm


class InicioView(TemplateView):
    """Vista para crear los productos no conformes"""

    template_name = 'Plasmotec/inicio.html'

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'Inicio'
        return context
        

class TestView(LoginRequiredMixin, TemplateView):

    template_name = 'Plasmotec/test.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{
                    'id':'',
                    'text':'--------------'
                }]
                # aca se debe realizar el filtro en los modelos
                # for i in SegundoModelo.objects.filter(llave_foraneasegundomodelo=request.POST['id'])
                #   data.append({'id':i.id, 'text': i.name, 'data':i.modelo.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(Nombre_producto__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.Nombre_producto
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | Django'
        context['form'] = TestForm()
        return context