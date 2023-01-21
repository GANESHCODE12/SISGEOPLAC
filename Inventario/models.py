"""Modelo Inventario"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user

#Modelos
from users.models import User


#Inventario Producto Terminado
class Inventario(models.Model):
  """Modelo Inventario"""

  inventario_creado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='inventario_creado_por'
  )
  fecha_creacion_inventario = models.DateTimeField(
    auto_now_add=True,
  )
  inventario_actualizado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='inventario_actualizado_por',
    null=True,
    blank=True,
    )
  fecha_actualizacion_inventario = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=True
    )
  producto = models.ForeignKey(
    'Productos.Productos_colores',
    on_delete=models.CASCADE,
    verbose_name='Producto',
  )
  cantidad_inicial = models.PositiveBigIntegerField(
    verbose_name="Cantidad inicial",
    null=True,
  )

  def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
    user = get_current_user()
    if user is not None:
      if not self.pk:
        self.inventario_creado_por = user
      else:
        self.inventario_actualizado_por = user
    return super(Inventario, self).save()

  def __str__(self):
    return str(self.producto)

  def toJSON(self):
    item = model_to_dict(self)
    return item

  class Meta:
    """Configuración del modelo"""

    verbose_name = 'Producto terminado'
    verbose_name_plural = 'Producto terminado'
    db_table = 'producto Terminado'
    ordering = ['-id']


class Requisicion_PT(models.Model):
  """Modelo InventarioRequisición de Producto Terminado"""

  requsicion_pt_creado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='requsicion_pt_creado_por'
  )
  fecha_requisicion_pt_inventario = models.DateTimeField(
    auto_now_add=True,
  )
  requisicion_pt_actualizado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='requisicion_pt_actualizado_por',
    null=True,
    blank=True,
    )
  fecha_actualizacion_requisicion_pt = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=True
    )
  orden = models.ForeignKey(
    'Produccion.Produccion',
    on_delete=models.CASCADE,
    verbose_name='Producto',
  )
  cantidad_solicitada = models.PositiveIntegerField(
    verbose_name='Cantidad Solicitada'
  )
  observaciones_PT = models.TextField(
    verbose_name='Observaciones',
    blank=True,
    null=True
  )

  def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
    user = get_current_user()
    if user is not None:
      if not self.pk:
        self.requsicion_pt_creado_por = user
      else:
        self.requisicion_pt_actualizado_por = user
    return super(Requisicion_PT, self).save()

  def __str__(self):
    return str(self.orden.producto)

  def toJSON(self):
    item = model_to_dict(self)
    return item

  class Meta:
    """Configuración del modelo"""

    verbose_name = 'Requisicion Producto Terminado'
    verbose_name_plural = 'Requisicion Producto Terminado'
    db_table = 'Requisicion Producto Terminado'
    ordering = ['-id']


#Inventario Materia Prima
class Materia_Prima_Insumo(models.Model):
  """Modelo Creación Materia Prima e insumos"""

  material_creado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='material_creado_por'
  )

  fecha_creacion_material = models.DateTimeField(
    auto_now_add=True,
  )

  material_actualizado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='material_actualizado_por',
    null=True,
    blank=True,
  )
    
  fecha_actualizacion_material = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=True
  )

  lista_categoria = [
    ('Materia Prima', 'Materia Prima'),
    ('Inusmo', 'Insumo'),
    ('Pigmento', 'Pigmento')
  ]

  categoria = models.CharField(
    max_length=30,
    choices=lista_categoria,
    verbose_name='Categoria'
  )

  nombre = models.CharField(
    max_length= 250,
    verbose_name='Material o Insumo',
  )

  referencia = models.CharField(
    max_length= 250,
    verbose_name='Referencia',
    default='N/A'
  )

  proveedor = models.CharField(
    max_length= 250,
    verbose_name='Proveedor',
  )

  Unidad_Meidida = models.CharField(
    max_length=5,
    verbose_name='Unidad de Medida',
    default='Kg'
  )

  def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
    user = get_current_user()
    if user is not None:
      if not self.pk:
        self.material_creado_por = user
      else:
        self.material_actualizado_por = user
    return super(Materia_Prima_Insumo, self).save()

  def __str__(self):
    return '{}, {}, {}'.format(
      self.nombre, self.referencia, self.categoria
    )

  def toJSON(self):
    item = model_to_dict(self)
    return item

  class Meta:
    """Configuración del modelo"""

    verbose_name = 'Materia Prima e Insumos'
    verbose_name_plural = 'Materia Prima e Insumos'
    db_table = 'Materia Prima e Insumos'
    ordering = ['-id']


class Requisicion(models.Model):
  """Modelo Solicitud de materia prima e insumos"""

  material_solicitado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='material_solicitado_por'
  )

  fecha_solicitud_material = models.DateTimeField(
    auto_now_add=True,
  )

  material_despachado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='material_despachado_por',
    null=True,
    blank=True,
    )
    
  fecha_despacho_material = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=True
    )

  material_solicitado = models.ForeignKey(
    'Inventario.Entrada',
    on_delete = models.CASCADE,
    verbose_name='Material Solicitado',
  )

  categoria = models.CharField(
    max_length= 250,
    verbose_name='Proveedor',
    default='Insumo'
  )

  cantidad_solicitada = models.FloatField(
    verbose_name='Cantidad solicitada'
  )

  numero_orden = models.ForeignKey(
    'Produccion.Produccion',
    on_delete=models.CASCADE,
    verbose_name='Orden de Producción'
  )

  observaciones_solicitud = models.TextField(
    blank=True,
    verbose_name='Observaciones Solicitud'
  )

  def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
    user = get_current_user()
    if user is not None:
      if not self.pk:
        self.material_solicitado_por = user
      else:
        self.material_despachado_por = user
    return super(Requisicion, self).save()

  def __str__(self):
    return str(self.material_solicitado)

  def toJSON(self):
    item = model_to_dict(self)
    item['solicitada'] = format(self.cantidad_solicitada, '.2f')
    item['solicitud'] = self.fecha_solicitud_material.strftime('%d/%m/%Y')
    item['despacho'] = self.fecha_despacho_material.strftime('%d/%m/%Y')
    return item

  class Meta:
    """Configuración del modelo"""

    verbose_name = 'Requsición'
    verbose_name_plural = 'Requisiciones'
    db_table = 'Requisiciones'
    ordering = ['-id']


class Entrada(models.Model):
  """Ingreso materia prima e insumos"""

  ingresado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='ingresado'
  )

  fecha_ingreso = models.DateTimeField(
    auto_now_add=True,
  )

  ingreso_actualizado_por = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='ingreso_actualizado_por',
    null=True,
    blank=True,
    )
    
  fecha_actualizacion_ingreso = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=True
    )

  ingreso_materia_prima = models.ForeignKey(
    'Inventario.Materia_Prima_Insumo',
    on_delete = models.CASCADE,
    verbose_name='Material Solicitado',
  )

  cantidad_ingresada = models.FloatField(
    verbose_name='Cantidad solicitada'
  )

  unidad_empaque = models.CharField(
    max_length= 10,
    verbose_name='Unidad de empaque',
    default='Kg'

  )

  factura = models.CharField(
    max_length=250,
    verbose_name='Factura',
    blank=True,
    null=True
  )

  remision = models.CharField(
    max_length=250,
    verbose_name='Remisión',
    blank=True,
    null=True
  )

  lote = models.CharField(
    max_length=250,
    verbose_name='lote',
    blank=True,
    null=True
  )

  observaciones_ingreso_materia_prima= models.TextField(
    blank=True,
    verbose_name='Observaciones Ingreso'
  )

  def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
    user = get_current_user()
    if user is not None:
      if not self.pk:
        self.ingresado_por = user
      else:
        self.ingreso_actualizado_por = user
    return super(Entrada, self).save()

  def __str__(self):
    return str(self.ingreso_materia_prima)

  def toJSON(self):
    item = model_to_dict(self)
    item['cantidad_ingresada'] = format(self.cantidad_ingresada, '.2f')
    item['ingreso'] = self.fecha_ingreso.strftime('%d/%m/%Y')
    return item

  class Meta:
    """Configuración del modelo"""

    verbose_name = 'Ingreso'
    verbose_name_plural = 'Ingresos'
    db_table = 'Ingresos'
    ordering = ['-id']
