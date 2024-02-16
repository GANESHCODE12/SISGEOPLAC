# Django
from django.http.response import JsonResponse
from django.db.models import Sum, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin

# Models
from Inventario.models import *
from Produccion.models import Produccion
from Control_produccion.models import ControlProduccion
from Control_calidad.models import MateriaPrimaInsumos
from PNC.models import ProductoNoConforme

# Form
from Inventario.forms import *

# Utils
import json


# Materia Prima e insumos
class ListaElementosMPInsumos(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  template_name = 'Inventario/lista_elementos.html'
  model = Materia_Prima_Insumo
  permission_required = 'add_inventario_materia_prima'

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
        for i in Materia_Prima_Insumo.objects.all():
          ingresos = Entrada.objects.all(
          ).filter(ingreso_materia_prima_id = i.id
          ).aggregate(ingreso_materia_prima_id = Sum('cantidad_ingresada'))

          requisiciones = Requisicion.objects.filter(material_solicitado__ingreso_materia_prima_id = i.id
          ).aggregate(material_solicitado__ingreso_materia_prima_id = Sum('cantidad_solicitada'))

          pnc = MateriaPrimaInsumos.objects.filter(
            materia_prima_insumo__ingreso_materia_prima_id = i.id
          ).aggregate(materia_prima_insumo__ingreso_materia_prima_id = Sum('materia_prima_insumo__cantidad_ingresada'))

          pnc_datos = MateriaPrimaInsumos.objects.filter(
            materia_prima_insumo__ingreso_materia_prima_id = i.id
          )

          def get_cantidad_pnc():
            for pnc_dato in pnc_datos:
              if pnc_dato.estado == 'Retenido' or pnc_dato.estado == 'En espera':
                cantidad_pnc = pnc['materia_prima_insumo__ingreso_materia_prima_id']
              else:
                cantidad_pnc = 0
              return cantidad_pnc

          item = i.toJSON()
          item['cantidad'] = (
            ingresos['ingreso_materia_prima_id'] - requisiciones['material_solicitado__ingreso_materia_prima_id']
            ) if requisiciones['material_solicitado__ingreso_materia_prima_id'] is not None else ingresos['ingreso_materia_prima_id']
          item['pnc'] = get_cantidad_pnc() if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None else 0
          if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None:
            if item['cantidad'] - item['pnc'] <= 0:
              item['cantidad_real'] = 0
            elif item['cantidad'] - item['pnc'] >= 0:
              item['cantidad_real'] = item['cantidad'] - item['pnc']
          else:
            item['cantidad_real'] = item['cantidad']
          data.append(item)
      elif action == 'search_details_entries':
        data = []
        for i in Entrada.objects.filter(ingreso_materia_prima_id = request.POST['id']):
          item = i.toJSON()
          item['persona'] = i.ingresado_por.get_full_name()
          item['nombre'] = i.ingreso_materia_prima.nombre
          item['referencia'] = i.ingreso_materia_prima.referencia
          data.append(item)
      elif action == 'search_details_outputs':
        data = []
        for i in Requisicion.objects.filter(material_solicitado__ingreso_materia_prima_id  = request.POST['id']):
          item = i.toJSON()
          item['persona'] = i.material_solicitado_por.get_full_name()
          item['nombre'] = i.material_solicitado.ingreso_materia_prima.nombre
          item['referencia'] = i.material_solicitado.ingreso_materia_prima.referencia
          data.append(item)
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Inventario Materia Prima e Insumos'
    context['list_url'] = reverse_lazy('Inventario:Lista_Elementos_MP_Insumos')
    context['entity'] = 'Inventario Materia Prima e Insumos'
    return context


class EntradaMPView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  model = Entrada
  template_name = 'Inventario/entradaMPI.html'
  success_url = reverse_lazy('Inventario:Lista_Elementos_MP_Insumos')
  permission_required = 'add_entrada'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
      data = {}
      try:
        action = request.POST['action']
        if action == 'search_MP_Insumo':
          data = []
          ids_exclude = json.loads(request.POST['ids'])
          busqueda = Materia_Prima_Insumo.objects.filter(
            Q(nombre__icontains=request.POST['term']) | 
            Q(referencia__icontains=request.POST['term'])
            ).exclude(id__in=ids_exclude)[0:10]
          for i in busqueda:
            item = i.toJSON()
            item['text'] = i.nombre
            item['referencia'] = i.referencia
            item['factura'] = ''
            item['remision'] = ''
            item['lote'] = ''
            item['observaciones_ingreso_materia_prima'] = ''
            data.append(item)
        elif action == 'add':
          with transaction.atomic():
            entradas = json.loads(request.POST['entradas'])

            for i in entradas['entrada']:
              ingreso = Entrada()
              ingreso.ingreso_materia_prima = Materia_Prima_Insumo.objects.get(id=i['id'])
              ingreso.cantidad_ingresada = float(i['cantidad_ingresada'])
              ingreso.factura = i['factura']
              ingreso.remision = i['remision']
              ingreso.lote = i['lote']
              ingreso.observaciones_ingreso_materia_prima = i['observaciones_ingreso_materia_prima']
              ingreso.save(self)
        elif action == 'create_element':
          with transaction.atomic():
            formElemento = CrearElementoForm(request.POST)
            data = formElemento.save(self)
        else:
          data['error'] = 'No ha ingresado a ninguna opción!'
      except Exception as e:
        data['error'] = str(e)
      return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Ingreso materia prima e insumos'
    context['list_url'] = reverse_lazy('Inventario:Lista_Elementos_MP_Insumos')
    context['entity'] = 'Ingreso MP e Insumos'
    context['action'] = 'add'
    context['formElemento'] = CrearElementoForm()
    return context


class Requision_MP_I(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  model = Requisicion
  template_name = 'Inventario/requision_MP.html'
  success_url = reverse_lazy('Inventario:Lista_Elementos_MP_Insumos')
  permission_required = 'add_requisicion'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
        instance_Requision_MP_I = form.save(commit=False)
        instance_Requision_MP_I.numero_orden = self.instance_Produccion
        instance_Requision_MP_I.save()

        return super(Requision_MP_I, self).form_valid(form)

  def get(self, request, *args, **kwargs):    
        self.instance_Produccion = get_object_or_404(Produccion, pk=kwargs.get('pk'))
        return super(Requision_MP_I, self).get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
      data = {}
      try:
        action = request.POST['action']
        if action == 'search_MP_Ingreso':
          data = []
          ids_exclude = json.loads(request.POST['ids'])
          busqueda = Entrada.objects.filter(
            Q(ingreso_materia_prima__nombre__icontains=request.POST['term']) | 
            Q(ingreso_materia_prima__referencia__icontains=request.POST['term']) |
            Q(lote__icontains=request.POST['term'])
          ).exclude(id__in=ids_exclude)[0:10]

          for i in busqueda:
            requisiciones = Requisicion.objects.filter(material_solicitado_id = i.id
            ).aggregate(material_solicitado_id = Sum('cantidad_solicitada'))
            pk = self.kwargs.get('pk')
            produccion = Produccion.objects.get(pk=pk)
            material = Requisicion.objects.filter(numero_orden_id=pk, categoria='Materia Prima').aggregate(numero_orden_id=Sum('cantidad_solicitada'))
            pigmento = Requisicion.objects.filter(numero_orden_id=pk, categoria='Pigmento').aggregate(numero_orden_id=Sum('cantidad_solicitada'))
            pnc = MateriaPrimaInsumos.objects.filter(
              materia_prima_insumo__ingreso_materia_prima_id = i.id
            ).aggregate(materia_prima_insumo__ingreso_materia_prima_id = Sum('materia_prima_insumo__cantidad_ingresada'))
            pnc_datos = MateriaPrimaInsumos.objects.filter(
              materia_prima_insumo__ingreso_materia_prima_id = i.id
            )

            def get_cantidad_pnc():
              for pnc_dato in pnc_datos:
                if pnc_dato.estado == 'Retenido' or pnc_dato.estado == 'En espera':
                  cantidad_pnc = pnc['materia_prima_insumo__ingreso_materia_prima_id']
                else:
                  cantidad_pnc = 0
                return cantidad_pnc

            def get_cantidad_disponible():
              if produccion.aprobacion_pigmento == True and i.ingreso_materia_prima.categoria == "Pigmento":
                return round((produccion.pigmento_adicional + produccion.maximo_pigmento) - pigmento['numero_orden_id'], 2)
              elif produccion.aprobacion_materia_prima == True and i.ingreso_materia_prima.categoria == "Materia Prima":
                return round((produccion.materia_prima_adicional + produccion.maximo_material) - material['numero_orden_id'], 2)
              elif i.ingreso_materia_prima.categoria == "Pigmento":
                return round(produccion.maximo_pigmento - pigmento['numero_orden_id'] if pigmento['numero_orden_id'] is not None else produccion.maximo_pigmento, 2)
              elif i.ingreso_materia_prima.categoria == "Materia Prima":
                return round(produccion.maximo_material - material['numero_orden_id'] if material['numero_orden_id'] is not None else produccion.maximo_material, 2)
              else:
                return round(i.cantidad_ingresada - requisiciones['material_solicitado_id'] if requisiciones['material_solicitado_id'] is not None else i.cantidad_ingresada, 2)
            
            def get_cantidad_inventario():
              if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None:
                resta_cantidad_disponible = get_cantidad_disponible() - get_cantidad_pnc()
                return 0 if resta_cantidad_disponible <= 0 else resta_cantidad_disponible
              elif get_cantidad_disponible() == 0:
                return 0
              elif pnc['materia_prima_insumo__ingreso_materia_prima_id'] is None:
                if requisiciones['material_solicitado_id'] is not None:
                  resta_inventario = i.cantidad_ingresada - requisiciones['material_solicitado_id']
                  return 0 if resta_inventario <= 0 else resta_inventario
                else:
                  return i.cantidad_ingresada

            item = i.toJSON()
            item['cantidad_disponible'] = get_cantidad_disponible()
            item['pnc'] = get_cantidad_pnc() if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None else 0
            item['cantidad_inventario'] = round(get_cantidad_inventario(), 2)
            item['text'] = i.ingreso_materia_prima.nombre
            item['referencia'] = i.ingreso_materia_prima.referencia
            item['tipo'] = i.ingreso_materia_prima.categoria
            item['cantidad_solicitada'] = 0
            item['observaciones_solicitud'] = ''
            data.append(item)
        elif action == 'add':
          with transaction.atomic():
            requisicion = json.loads(request.POST['solicitudes'])

            for i in requisicion['requisicion']:
              solicitado = Requisicion()
              solicitado.material_solicitado = Entrada.objects.get(id=i['id'])
              solicitado.cantidad_solicitada = float(i['cantidad_solicitada'])
              solicitado.numero_orden_id = self.kwargs.get('pk')
              solicitado.observaciones_solicitud = i['observaciones_solicitud']
              solicitado.categoria = i['tipo']
              solicitado.save(self)
        else:
          data['error'] = 'No ha ingresado a ninguna opción!'
      except Exception as e:
        data['error'] = str(e)
      return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    pk = self.kwargs.get('pk')
    context = super().get_context_data(**kwargs)
    context['produccion'] = Produccion.objects.get(pk=pk)
    context['title'] = 'Solicitud Materia Prima E Insumos'
    context['list_url'] =self.success_url
    context['entity'] = 'Solicitud MP e Insumos'
    context['action'] = 'add'
    return context


class ReportMPIView(TemplateView):
  template_name = 'Inventario/report_mpi.html'

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
        search = Materia_Prima_Insumo.objects.all()
        if len(start_date) and len(end_date):
          search = search.filter(fecha_actualizacion_material__range=[start_date, end_date])
        for i in search:
          ingresos = Entrada.objects.all(
          ).filter(ingreso_materia_prima_id = i.id
          ).aggregate(ingreso_materia_prima_id = Sum('cantidad_ingresada'))

          requisiciones = Requisicion.objects.filter(material_solicitado__ingreso_materia_prima_id = i.id
          ).aggregate(material_solicitado__ingreso_materia_prima_id = Sum('cantidad_solicitada'))

          pnc = MateriaPrimaInsumos.objects.filter(
            materia_prima_insumo__ingreso_materia_prima_id = i.id
          ).aggregate(materia_prima_insumo__ingreso_materia_prima_id = Sum('materia_prima_insumo__cantidad_ingresada'))

          pnc_datos = MateriaPrimaInsumos.objects.filter(
            materia_prima_insumo__ingreso_materia_prima_id = i.id
          )

          def get_cantidad_pnc():
            for pnc_dato in pnc_datos:
              if pnc_dato.estado == 'Retenido' or pnc_dato.estado == 'En espera':
                cantidad_pnc = pnc['materia_prima_insumo__ingreso_materia_prima_id']
              else:
                cantidad_pnc = 0
              return cantidad_pnc

          item = i.toJSON()
          item['Unidad_Meidida'] = i.Unidad_Meidida
          item['cantidad'] = (
            ingresos['ingreso_materia_prima_id'] - requisiciones['material_solicitado__ingreso_materia_prima_id']
            ) if requisiciones['material_solicitado__ingreso_materia_prima_id'] is not None else ingresos['ingreso_materia_prima_id']
          item['pnc'] = get_cantidad_pnc() if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None else 0
          if pnc['materia_prima_insumo__ingreso_materia_prima_id'] is not None:
            if item['cantidad'] - item['pnc'] <= 0:
              item['cantidad_real'] = 0
            elif item['cantidad'] - item['pnc'] >= 0:
              item['cantidad_real'] = item['cantidad'] - item['pnc']
          else:
            item['cantidad_real'] = item['cantidad']
          data.append(item)
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Reporte Inventario Materia Prime E Insumos'
    context['entity'] = 'Reportes'
    context['list_url'] = reverse_lazy('Reportes')
    context['form'] = ReportMpiForm()
    return context


class Ingresos(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  template_name = 'Inventario/lista_ingresos.html'
  model = Entrada
  permission_required = 'view_materiaprimainsumos'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'searchdata':
        data = []
        ids = []
        for i in Entrada.objects.all():
          item = i.toJSON()
          for inspeccion in MateriaPrimaInsumos.objects.filter(materia_prima_insumo = i.id):
            ids.append(inspeccion.materia_prima_insumo_id)
          item['referencia'] = i.ingreso_materia_prima.referencia
          item['unidad_medida'] = i.ingreso_materia_prima.Unidad_Meidida
          item['inspeccion'] = inspeccion.id if i.id in ids else 0
          item['material'] = i.ingreso_materia_prima.nombre
          item['categoria'] = i.ingreso_materia_prima.categoria
          item['existe'] = 1 if i.id in ids else 0
          data.append(item)
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Ingresos'
    context['list_url'] = reverse_lazy('Inventario:Ingresos')
    context['entity'] = 'Ingresos'
    return context


class ListaProductoTerminado(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  template_name = 'Inventario/lista_productos.html'
  model = Inventario
  permission_required = 'view_inventario'

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

        for i in Inventario.objects.all():
          ing = ControlProduccion.objects.filter(
            numero_op__producto_id = i.producto_id,
            fecha_creacion__year__gt = 2022
          ).aggregate(numero_op__producto_id = Sum('cantidad_producida'))

          req = Requisicion_PT.objects.filter(orden__producto_id = i.producto_id
          ).aggregate(orden__producto_id = Sum('cantidad_solicitada'))

          pnc = ProductoNoConforme.objects.filter(
            id_inspeccion__numero_op__producto_id = i.producto_id
          ).aggregate(id_inspeccion__numero_op__producto_id = Sum('cantidad_pnc'))

          def calculo_cantidad():
            if ing['numero_op__producto_id'] is not None and req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
              return (i.cantidad_inicial + ing['numero_op__producto_id']) - req['orden__producto_id']
            elif req['orden__producto_id'] is not None and ing['numero_op__producto_id'] is not None:
              return  ing['numero_op__producto_id'] - req['orden__producto_id']
            elif req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
              return i.cantidad_inicial - req['orden__producto_id']
            elif ing['numero_op__producto_id'] is not None and i.cantidad_inicial is not None:
              return ing['numero_op__producto_id'] + i.cantidad_inicial
            elif i.cantidad_inicial is not None:
              return i.cantidad_inicial
            elif ing['numero_op__producto_id'] is not None:
              return ing['numero_op__producto_id']
            elif req['orden__producto_id'] is not None:
              return req['orden__producto_id']
            else:
              return 0

          item = i.toJSON()
          item['cantidad'] = calculo_cantidad()
          item['nombre'] = i.producto.productos.Nombre_producto
          item['color'] = i.producto.color.color
          item['codigo'] = i.producto.codigo_producto
          item['unidad_empaque'] = i.producto.productos.unidad_empaque
          item['cantidad_pnc'] = pnc['id_inspeccion__numero_op__producto_id'] if pnc['id_inspeccion__numero_op__producto_id'] is not None else 0
          data.append(item)
      elif action == 'search_details_entries':
        data = []
        for i in ControlProduccion.objects.filter(numero_op__producto_id = request.POST['producto_id']):
          item = i.toJSON()
          item['nombre'] = i.numero_op.producto.productos.Nombre_producto
          item['producto_id'] = i.numero_op.producto_id
          item['lote'] = '{}-{}'.format(i.numero_op_id, i.numero_op.fecha_creacion.year)
          item['fecha_ingreso'] = i.fecha_creacion.strftime('%d/%m/%Y')
          item['orden'] = i.numero_op_id
          item['color'] = i.numero_op.producto.color.color
          item['cantidad'] = i.cantidad_producida
          data.append(item)
      elif action == 'search_details_outputs':
        data = []
        for i in Requisicion_PT.objects.filter(orden__producto_id  = request.POST['producto_id']):
          item = i.toJSON()
          item['persona'] = i.requsicion_pt_creado_por.get_full_name()
          item['producto_id'] = i.orden.producto_id
          item['nombre'] = i.orden.producto.productos.Nombre_producto
          item['color'] = i.orden.producto.color.color
          item['fecha_solicitud'] = i.fecha_requisicion_pt_inventario.strftime('%d/%m/%Y')
          data.append(item)
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Inventario Producto Terminado'
    context['list_url'] = reverse_lazy('Inventario:Inventario_PT')
    context['entity'] = 'Inventario Producto Terminado'
    return context


class ListaProductoTerminadoOrden(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  template_name = 'Inventario/lista_productos_orden.html'
  model = Produccion
  permission_required = 'view_produccion'

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
          ingresos = ControlProduccion.objects.all(
          ).filter(
            numero_op_id = i.numero_op,
            fecha_creacion__year__gt = 2022
          ).aggregate(numero_op_id = Sum('cantidad_producida'))

          requisiciones = Requisicion_PT.objects.all(
          ).filter(orden_id = i.numero_op
          ).aggregate(orden_id = Sum('cantidad_solicitada'))

          def calculo_cantidad_orden():
            if ingresos['numero_op_id'] is not None and requisiciones['orden_id'] is not None:
              return ingresos['numero_op_id'] - requisiciones['orden_id']
            elif requisiciones['orden_id'] is not None:
              return  requisiciones['orden_id']
            elif ingresos['numero_op_id'] is not None:
              return  ingresos['numero_op_id']
            else:
              return 0
          
          #incluir en master
          def calculo_cantidad_cajas():
            if ingresos['numero_op_id'] is not None and requisiciones['orden_id'] is not None:
              cantidad = ingresos['numero_op_id'] - requisiciones['orden_id']
              return cantidad/i.producto.productos.unidad_empaque
            elif requisiciones['orden_id'] is not None:
              cantidad = requisiciones['orden_id']
              return  cantidad/i.producto.productos.unidad_empaque
            elif ingresos['numero_op_id'] is not None:
              cantidad = ingresos['numero_op_id']
              return  cantidad/i.producto.productos.unidad_empaque
            else:
              return 0

          item = i.toJSON()
          if calculo_cantidad_orden() > 0:
            item['cantidad'] = calculo_cantidad_orden()
            item['numero_op'] = i.numero_op
            item['lote'] = '{}-{}'.format(i.numero_op, i.fecha_creacion.year)
            item['nombre'] = i.producto.productos.Nombre_producto
            item['color'] = i.producto.color.color
            item['codigo'] = i.producto.codigo_producto
            item['cajas'] = calculo_cantidad_cajas()
            data.append(item)
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Inventario Por Orden'
    context['list_url'] = reverse_lazy('Inventario:inventario-producto-terminado-orden')
    context['entity'] = 'Inventario Por Orden'
    return context


class Requision_PT_View(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

  model = Requisicion_PT
  template_name = 'Inventario/requision_PT.html'
  success_url = reverse_lazy('Inventario:Inventario_PT')
  permission_required = 'add_requisicion_pt'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
      data = {}
      try:
        action = request.POST['action']
        if action == 'search_PT':
          data = []
          ids_exclude = json.loads(request.POST['ids'])
          busqueda = Inventario.objects.filter(
            Q(producto__productos__Nombre_producto__icontains=request.POST['term']) | 
            Q(producto__codigo_producto__icontains=request.POST['term']) |
            Q(producto__color__color__icontains=request.POST['term'])
          ).exclude(id__in=ids_exclude)[0:10]

          for i in busqueda:
            ing = ControlProduccion.objects.filter(numero_op__producto_id = i.producto_id
            ).aggregate(numero_op__producto_id = Sum('cantidad_producida'))

            pnc = ProductoNoConforme.objects.filter(
              id_inspeccion__numero_op__producto_id = i.producto_id
            ).aggregate(id_inspeccion__numero_op__producto_id = Sum('cantidad_pnc'))

            ordenes = ControlProduccion.objects.filter(numero_op__producto_id = i.producto_id)

            req = Requisicion_PT.objects.filter(orden__producto_id = i.producto_id
            ).aggregate(orden__producto_id = Sum('cantidad_solicitada'))

            def calculo_cantidad():
              if ing['numero_op__producto_id'] is not None and req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
                return (i.cantidad_inicial + ing['numero_op__producto_id']) - req['orden__producto_id']
              elif req['orden__producto_id'] is not None and ing['numero_op__producto_id'] is not None:
                return  ing['numero_op__producto_id'] - req['orden__producto_id']
              elif req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
                return i.cantidad_inicial - req['orden__producto_id']
              elif ing['numero_op__producto_id'] is not None and i.cantidad_inicial is not None:
                return ing['numero_op__producto_id'] + i.cantidad_inicial
              elif i.cantidad_inicial is not None:
                return i.cantidad_inicial
              elif ing['numero_op__producto_id'] is not None:
                return ing['numero_op__producto_id']
              elif req['orden__producto_id'] is not None:
                return req['orden__producto_id']
              else:
                return 0

            item = i.toJSON()
            item['text'] = i.producto.productos.Nombre_producto
            item['color'] = i.producto.color.color
            item['cantidad_disponible'] = calculo_cantidad() - pnc['id_inspeccion__numero_op__producto_id'] if pnc['id_inspeccion__numero_op__producto_id'] is not None else calculo_cantidad()
            item['codigo_producto'] = i.producto.codigo_producto
            item['pnc'] = pnc['id_inspeccion__numero_op__producto_id'] if pnc['id_inspeccion__numero_op__producto_id'] is not None else 0
            for orden in ordenes:
              item['orden'] = orden.numero_op_id
            item['cantidad_solicitada'] = 0.00
            item['observaciones_PT'] = ''
            data.append(item)
        elif action == 'add':
          with transaction.atomic():
            requisicion = json.loads(request.POST['solicitudes_pt'])

            for i in requisicion['requisicion_pt']:
              solicitado = Requisicion_PT()
              solicitado.orden_id = int(i['orden'])
              solicitado.cantidad_solicitada = float(i['cantidad_solicitada'])
              solicitado.observaciones_PT = i['observaciones_PT']
              solicitado.save(self)
        else:
          data['error'] = 'No ha ingresado a ninguna opción!'
      except Exception as e:
        data['error'] = str(e)
      return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Solicitud Producto Terminado'
    context['list_url'] =self.success_url
    context['entity'] = 'Solicitud Producto Terminado'
    context['action'] = 'add'
    return context


class ReportPTView(TemplateView):
  template_name = 'Inventario/report_pt.html'

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
        search = Inventario.objects.all()
        if len(start_date) and len(end_date):
          search = search.filter(fecha_actualizacion_inventario__range=[start_date, end_date])
        for i in search:
          ing = ControlProduccion.objects.all(
          ).filter(numero_op__producto_id = i.producto_id
          ).aggregate(numero_op__producto_id = Sum('cantidad_producida'))

          req = Requisicion_PT.objects.all(
          ).filter(orden__producto_id = i.producto_id
          ).aggregate(orden__producto_id = Sum('cantidad_solicitada'))

          pnc = ProductoNoConforme.objects.filter(
            id_inspeccion__numero_op__producto_id = i.producto_id
          ).aggregate(id_inspeccion__numero_op__producto_id = Sum('cantidad_pnc'))

          def calculo_cantidad():
            if ing['numero_op__producto_id'] is not None and req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
              return (i.cantidad_inicial + ing['numero_op__producto_id']) - req['orden__producto_id']
            elif req['orden__producto_id'] is not None and ing['numero_op__producto_id'] is not None:
              return  ing['numero_op__producto_id'] - req['orden__producto_id']
            elif req['orden__producto_id'] is not None and i.cantidad_inicial is not None:
              return i.cantidad_inicial - req['orden__producto_id']
            elif ing['numero_op__producto_id'] is not None and i.cantidad_inicial is not None:
              return ing['numero_op__producto_id'] + i.cantidad_inicial
            elif i.cantidad_inicial is not None:
              return i.cantidad_inicial
            elif ing['numero_op__producto_id'] is not None:
              return ing['numero_op__producto_id']
            elif req['orden__producto_id'] is not None:
              return req['orden__producto_id']
            else:
              return 0

          cantidad_pnc = pnc['id_inspeccion__numero_op__producto_id'] if pnc['id_inspeccion__numero_op__producto_id'] is not None else 0

          data.append([
            i.producto.codigo_producto,
            i.producto.productos.Nombre_producto,
            i.producto.color.color,
            i.producto.productos.unidad_empaque,
            calculo_cantidad(),
            cantidad_pnc,
            0 if calculo_cantidad() == 0 else calculo_cantidad() - cantidad_pnc,
          ])
      else:
        data['error'] = 'Ha ocurrido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Reporte Inventario Producto Terminado'
    context['entity'] = 'Reportes'
    context['list_url'] = reverse_lazy('Reportes')
    context['form'] = ReportPTForm()
    return context
