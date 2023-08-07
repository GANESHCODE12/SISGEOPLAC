"""Vistas de la aplicación de productos"""

# Django
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Form
from Productos.forms import *

#Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# Models
from Productos.models import *

#Utilidades
import json


#Listas
class ListaProductoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de fichas técnicas"""

    template_name = 'Productos/lista_productos.html'
    model = Producto
    permission_required = 'view_producto'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Producto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Productos'
        return context


class ListaDimensiones(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de fichas técnicas"""

    template_name = 'Productos/lista_dimensiones.html'
    model = Dimensiones
    permission_required = 'view_dimensiones'


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de dimensiones'
        context['list_url'] = reverse_lazy('Productos:Dimensiones')
        context['entity'] = 'Dimensiones'
        return context


class ListaAtributos(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de fichas técnicas"""

    template_name = 'Productos/lista_atributos.html'
    model = Atributos
    permission_required = 'view_atributos'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de atributos'
        context['list_url'] = reverse_lazy('Productos:Atributos')
        context['entity'] = 'Atributos'
        return context


class ListaPruebas(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de fichas técnicas"""

    template_name = 'Productos/lista_pruebas.html'
    model = Pruebas
    permission_required = 'view_pruebas'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de pruebas'
        context['list_url'] = reverse_lazy('Productos:Pruebas')
        context['entity'] = 'Dimensiones'
        return context


class ListaNormas(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    """Vista para lista de fichas técnicas"""

    template_name = 'Productos/lista_normas.html'
    model = Normas
    permission_required = 'view_normas'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de normas'
        context['list_url'] = reverse_lazy('Productos:Normas')
        context['entity'] = 'Normas'
        return context


class ListaColorView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'Productos/lista_colores.html'
    model = Colores
    permission_required = 'view_colores'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de colores'
        context['list_url'] = reverse_lazy('Productos:Colores')
        context['entity'] = 'Colores'
        return context


#Detalle
class DetalleFichaView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    """Vista para el detalle de las fichas técnicas"""

    model = Producto
    queryset = Producto.objects.all()
    context_object_name = 'FichasTecnica'
    permission_required = 'view_producto'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_template_names(self):
        pk = self.kwargs.get('pk')
        producto_color = Productos_colores.objects.filter(productos_id=pk)

        for document in producto_color:
            if document.version_documento == 1:
                return 'Productos/detalle_ficha.html'
            elif document.version_documento == 2:
                return 'Productos/detalle_ficha_V3.html'

    def get_context_data(self, **kwargs):
        """Agrega los demás modelos relacionados con la ficha
        técnica"""

        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['caracteristicasdimensionale'] = CaracteristicasDimensionale.objects.all().filter(id_producto_c=pk)
        context['pruebasensayo'] = PruebasEnsayo.objects.all().filter(id_producto_p=pk)
        context['controlatributo'] = ControlAtributo.objects.all().filter(id_producto_a=pk)
        context['normasaplicable'] = NormasAplicable.objects.all().filter(id_producto_n=pk)
        context['color'] = Productos_colores.objects.all().filter(productos_id=pk)
        context['title'] = 'Detalle Producto'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Productos'
        return context


#Actualizar
class ActualizarFichaTecnica(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    model = Producto
    form_class = ActualizarProductoForm
    template_name = 'Productos/actualizar_plano.html'
    success_url = reverse_lazy('Productos:Productos')
    context_object_name = 'Producto'
    permission_required = 'change_producto'

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
        """Agrega la información a la vista de actualización"""
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Ficha'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Productos'
        context['action'] = 'edit'
        return context


class ActualizarDiagramaView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):

    model = Producto
    form_class = ActualizarDiagramaForm
    template_name = 'Productos/actualizar_plano.html'
    success_url = reverse_lazy('Productos:Productos')
    context_object_name = 'Producto'
    permission_required = 'change_producto'

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
        """Agrega la información a la vista de actualización"""
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Diagrama'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Productos'
        context['action'] = 'edit'
        return context


#Crear
class NuevoProductoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = Producto
    form_class = CrearProductoForm
    template_name = 'Productos/crear_producto.html'
    success_url = reverse_lazy('Productos:Productos')
    permission_required = 'add_producto'

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
        context['title'] = 'Nuevo Producto'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Productos'
        context['action'] = 'add'
        return context


class NuevaDimensionView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las caracteristricas dimesionales
    de las fichas técnicas"""

    model = Dimensiones
    form_class = DimensionesForm
    permission_required = 'add_dimensiones'
    template_name = 'Productos/dimensiones_ficha.html'
    success_url = reverse_lazy('Productos:Dimensiones')

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
        context['title'] = 'Nuevas dimensiones'
        context['list_url'] = reverse_lazy('Productos:Dimensiones')
        context['entity'] = 'Dimensiones'
        context['action'] = 'add'
        return context


class NuevaPruebaView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
        """Vista para crear las pruebas y/o ensayos de las
        fichas técnicas"""

        model = Pruebas
        form_class = PruebasForm
        permission_required = 'view_pruebas'
        template_name = 'Productos/pruebas.html'
        success_url = reverse_lazy('Productos:Pruebas')

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
            context['title'] = 'Nuevas pruebas'
            context['list_url'] = reverse_lazy('Productos:Pruebas')
            context['entity'] = 'Pruebas'
            context['action'] = 'add'
            return context


class NuevoAtributoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
        """Vista para crear controles a los atributos de las
        fichas técnicas"""

        model = Atributos
        form_class = AtributosForm
        permission_required = 'add_atributos'
        template_name = 'Productos/control.html'
        success_url = reverse_lazy('Productos:Atributos')

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
            context['title'] = 'Nuevos atributos'
            context['list_url'] = reverse_lazy('Productos:Atributos')
            context['entity'] = 'Atributos'
            context['action'] = 'add'
            return context


class NuevaNormaView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
        """Vista para crear controles a los atributos de las
        fichas técnicas"""

        model = Normas
        form_class = NormasForm
        permission_required = 'add_normas'
        template_name = 'Productos/normas.html'
        success_url = reverse_lazy('Productos:Normas')

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
            context['title'] = 'Nuevas normas'
            context['list_url'] = reverse_lazy('Productos:Normas')
            context['entity'] = 'Productos'
            context['action'] = 'add'
            return context


class NuevaFichaTecnica(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = Producto
    form_class = CrearProductoForm
    template_name = 'Productos/crear_ficha_tecnica.html'
    success_url = reverse_lazy('Productos:Producto')
    permission_required = 'add_producto'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_normas':
                data = []
                ids_exclude = json.loads(request.POST['ids_normas'])
                busqueda = Normas.objects.filter(
                    titulo__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.titulo
                    data.append(item)
            elif action == 'search_pruebas':
                data = []
                ids_exclude = json.loads(request.POST['ids_pruebas'])
                busqueda = Pruebas.objects.filter(
                    variables__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.variables
                    data.append(item)
            elif action == 'search_dimensiones':
                data = []
                ids_exclude = json.loads(request.POST['ids_dimensiones'])
                busqueda = Dimensiones.objects.filter(
                    caracteristicas_control__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.caracteristicas_control
                    data.append(item)
            elif action == 'search_atributos':
                data = []
                ids_exclude = json.loads(request.POST['ids_atributos'])
                busqueda = Atributos.objects.filter(
                    caracteristicas__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.caracteristicas
                    data.append(item)
            elif action == 'search_colores':
                data = []
                ids_exclude = json.loads(request.POST['ids_colores'])
                busqueda = Colores.objects.filter(
                    color__icontains=request.POST['term']
                ).exclude(id__in=ids_exclude)[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.color
                    item['codigo_producto'] = ''
                    data.append(item)
            elif action == 'search_producto':
                data = []
                busqueda = Producto.objects.filter(
                    Nombre_producto__icontains=request.POST['term']
                )[0:10]
                for i in busqueda:
                    item = i.toJSON()
                    item['text'] = i.Nombre_producto
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    ficha = json.loads(request.POST['ficha'])

                    producto = Producto()
                    producto.Nombre_producto = ficha['Nombre_producto']
                    producto.numero_ficha = int(ficha['numero_ficha'])
                    producto.proceso = ficha['proceso']
                    producto.proceso = ficha['proceso']
                    producto.version = int(ficha['version'])
                    producto.fecha_vigencia = ficha['fecha_vigencia']
                    producto.tipo_producto = ficha['tipo_producto']
                    producto.cliente_especifico = ficha['cliente_especifico']
                    producto.estado_ficha = ficha['estado_ficha']
                    producto.cavidades = int(ficha['cavidades'])
                    producto.peso = float(ficha['peso'])
                    producto.material = ficha['material']
                    producto.ciclo = int(ficha['ciclo'])
                    producto.descripción_especificaciones = ficha['descripción_especificaciones']
                    producto.olor = ficha['olor']
                    producto.pigmento = ficha['pigmento']
                    producto.tipo = ficha['tipo']
                    producto.unidad_empaque = int(ficha['unidad_empaque'])
                    producto.forma_empaque = ficha['forma_empaque']
                    producto.caja = ficha['caja']
                    producto.bolsa = ficha['bolsa']
                    producto.plano = ficha['plano']
                    producto.fecha_plano = ficha['fecha_plano']
                    producto.vida_util = ficha['vida_util']
                    producto.elaborado = ficha['elaborado']
                    producto.revisado = ficha['revisado']
                    producto.aprobado = ficha['aprobado']
                    producto.notas = ficha['notas']
                    producto.save()

                    for i in ficha['normas']:
                        normas = NormasAplicable()
                        normas.id_producto_n_id = producto.id
                        normas.id_norma_id = i['id']
                        normas.save(self)

                    for i in ficha['dimensiones']:
                        dimensiones = CaracteristicasDimensionale()
                        dimensiones.id_producto_c_id = producto.id
                        dimensiones.id_dimensiones_id = i['id']
                        dimensiones.valor_nominal = float(i['valor_nominal'])
                        dimensiones.tolerancia_d = float(i['tolerancia_d'])
                        dimensiones.save(self)

                    for i in ficha['pruebas']:
                        pruebas = PruebasEnsayo()
                        pruebas.id_producto_p_id = producto.id
                        pruebas.id_pruebas_id = i['id']
                        pruebas.valor = float(i['valor'])
                        pruebas.tolerancia_p = float(i['tolerancia_p'])
                        pruebas.save(self)

                    for i in ficha['atributos']:
                        atributos = ControlAtributo()
                        atributos.id_producto_a_id = producto.id
                        atributos.id_atributo_id = i['id']
                        atributos.save(self)

                    for i in ficha['colores']:
                        colores_productos = Productos_colores()
                        colores_productos.color_id = i['id']
                        colores_productos.productos_id = producto.id
                        colores_productos.codigo_producto = i['codigo_producto']
                        colores_productos.save(self)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva ficha técnica'
        context['list_url'] = reverse_lazy('Productos:Productos')
        context['entity'] = 'Fichas Técnicas'
        context['action'] = 'add'
        return context


class NuevoColorView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Colores
    form_class = ColorForm
    permission_required = 'add_colores'
    template_name = 'Productos/color.html'
    success_url = reverse_lazy('Productos:Colores')

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
        context['title'] = 'Nuevo Color'
        context['list_url'] = reverse_lazy('Productos:Colores')
        context['entity'] = 'Colores'
        context['action'] = 'add'
        return context


class ProductoColorView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
        model = Productos_colores
        form_class = ProductosColoresForm
        permission_required = 'add_productos_colores'
        template_name = 'Productos/productos_colores.html'
        success_url = reverse_lazy('Productos:Productos')

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
            context['title'] = 'Relacionar producto con color'
            context['list_url'] = self.success_url
            context['entity'] = 'Productos'
            context['action'] = 'add'
            return context
