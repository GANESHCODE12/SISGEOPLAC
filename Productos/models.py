"""Modelo de productos"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user
from django.conf import settings


class Producto(models.Model):
    """Modelo de los datos generales del producto"""

    elaborado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='elaborado_por'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='modificado_por',
        on_delete = models.CASCADE,
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    """Información General"""
    Nombre_producto = models.CharField(
        max_length=255,
        verbose_name='Nombre del Producto'
    )
    numero_ficha = models.PositiveIntegerField(
        unique=True,
        verbose_name='Número de ficha'
    )
    codigo_producto = models.CharField(
        max_length=255,
        verbose_name='Código de producto'
    )
    proceso = models.CharField(
        max_length=50,
        verbose_name='Proceso'
    )
    version = models.PositiveIntegerField(
        verbose_name='Versión'
    )
    fecha_vigencia = models.DateField(
        verbose_name='Fecha de vigencia'
    )
    tipo_producto = models.CharField(
        max_length=20,
        verbose_name='Tipo de producto'
    )
    cliente_especifico = models.CharField(
        max_length=40,
        verbose_name='Cliente'
    )
    
    lista_estado_ficha = [
        ('Vigente','Vigente'),
        ('Obsoleto','Obsoleto'),
        ('En aprobación','En aprobación'),
        ('En revisión','En revisión'),
    ]
    estado_ficha = models.CharField(
        max_length=40,
        choices=lista_estado_ficha,
        verbose_name='Estado de ficha',
        default='Vigente'
    )

    """Especificaciones"""
    cavidades = models.PositiveIntegerField(
        verbose_name='Cavidades'
    )
    peso = models.FloatField(
        verbose_name='Peso'
    )
    material = models.CharField(
        max_length=255,
        verbose_name='Material'
    )
    ciclo = models.PositiveIntegerField(
        verbose_name='Ciclo'
    )
    descripción_especificaciones = models.CharField(
        max_length=255,
        verbose_name='Descripción de especificaciones'
    )

    """Caracteristicas organolepticas"""
    color = models.CharField(
        max_length=60,
        default='Según lo acordado por el cliente',
        verbose_name='Color'
    )
    olor = models.CharField(
        max_length=255,
        verbose_name='Olor'
    )
    sabor = models.CharField(
        max_length=255,
        verbose_name='Sabor'
    )
    pigmento = models.CharField(
        max_length=255,
        verbose_name='Pigmento'
    )

    """Unidad de empaque"""
    tipo = models.CharField(
        max_length=255,
        verbose_name='Tipo'
    )
    unidad_empaque = models.PositiveIntegerField(
        verbose_name='Unidad de empaque'
    )
    forma_empaque = models.CharField(
        max_length=255,
        verbose_name='Forma de empaque'
    )
    caja = models.CharField(
        max_length=255,
        verbose_name='Tamaño de caja'
    )
    bolsa = models.CharField(
        max_length=255,
        verbose_name='Tipo de bolsa'
    )

    """Caracteristicas de control"""
    plano = models.CharField(
        max_length=255,
        verbose_name='Código del plano'
    )
    fecha_plano = models.DateField(
        verbose_name='Fecha del plano'
    )
    diagrama = models.ImageField(
        upload_to='Produccion/plane',
        verbose_name='Diagrama'
    )

    """Condiciones de almacenamiento"""
    vida_util = models.TextField(
        blank=True,
        verbose_name='Vida útil'
    )

    """Control del documento"""
    elaborado = models.CharField(
        max_length=255,
        verbose_name='Elaborado por'
    )
    revisado = models.CharField(
        max_length=255,
        verbose_name='Revisado por'
    )
    aprobado = models.CharField(
        max_length=255,
        verbose_name='Aprobado por'
    )
    notas = models.TextField(
        blank=True,
        verbose_name='Notas'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.elaborado_por = user
            else:
                self.modificado_por = user
        return super(Producto, self).save()

    def __str__(self):
        return '{} V.{}, Cliente: {}'.format(
            self.Nombre_producto, str(self.version), self.cliente_especifico
        )

    def toJSON(self):
        item = model_to_dict(
            self, 
            exclude=[
                'diagrama'
            ]
        )
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'
        ordering = ['-id']


class CaracteristicasDimensionale(models.Model):
    """Modelo de las caracteristicas dimensionales del producto"""

    elaborado_por_c = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='elaborado_por_c',
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    modificado_por_c = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='modificado_por_c',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_producto_c = models.ForeignKey(
        'Productos.Producto',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto'
    )

    id_dimensiones = models.ForeignKey(
        'Productos.Dimensiones',
        on_delete=models.CASCADE,
        verbose_name='Dimensión'
    )

    valor_nominal = models.FloatField(
        verbose_name='Valor nominal',
    )

    tolerancia_d = models.FloatField(
        verbose_name='Tolerancia',
    )

    def __str__(self):
        return self.id_dimensiones.caracteristicas_control

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.elaborado_por_c = user
            else:
                self.modificado_por_c = user
        return super(CaracteristicasDimensionale, self).save()
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Caracteristica dimensional'
        verbose_name_plural = 'Caracteristicas dimensionales'
        db_table = 'Caracteristicas dimensionales'
        ordering = ['-id']


class PruebasEnsayo(models.Model):
    """Modelo de las pruebas que se deben realizar al producto"""

    elaborado_por_p = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='elaborado_por_p',
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    modificado_por_p = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='modificado_por_p',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_producto_p = models.ForeignKey(
        'Productos.Producto',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto'
    )

    id_pruebas = models.ForeignKey(
        'Productos.Pruebas',
        on_delete=models.CASCADE,
        verbose_name='Prueba y/o ensayo'
    )

    valor = models.FloatField(
        verbose_name='Valor',
    )

    tolerancia_p = models.FloatField(
        verbose_name='Tolerancia',
    )

    def __str__(self):
        return self.id_pruebas.variables

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.elaborado_por_p = user
            else:
                self.modificado_por_p = user
        return super(PruebasEnsayo, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Prueba y/o Ensayo'
        verbose_name_plural = 'Pruebas y/o Ensayos'
        db_table = 'Prueba_Ensayo'
        ordering = ['-id']


class ControlAtributo(models.Model):
    """Modelos de atributos que se deben controlar"""

    elaborado_por_ca = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='elaborado_por_ca',
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    modificado_por_ca = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='modificado_por_ca',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_producto_a = models.ForeignKey(
        'Productos.Producto',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto'
    )

    id_atributo = models.ForeignKey(
        'Productos.Atributos',
        on_delete=models.CASCADE,
        verbose_name='Atributo'
    )

    def __str__(self):
        return self.id_atributo.caracteristicas

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.elaborado_por_ca = user
            else:
                self.modificado_por_ca = user
        return super(ControlAtributo, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Control atributo'
        verbose_name_plural = 'Controles de atributo'
        db_table = 'Control Atributo'
        ordering = ['-id']


class NormasAplicable(models.Model):
    """Modelo de las normas que aplican al producto"""

    elaborado_por_n = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='elaborado_por_n',
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    modificado_por_n = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='modificado_por_n',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_producto_n = models.ForeignKey(
        'Productos.Producto',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto'
    )

    id_norma = models.ForeignKey(
        'Productos.Normas',
        on_delete=models.CASCADE,
        verbose_name='Norma'
    )

    def __str__(self):
        return self.id_norma.titulo

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.elaborado_por_n = user
            else:
                self.modificado_por_n = user
        return super(NormasAplicable, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Normas Aplicables'
        verbose_name_plural = 'Normas Aplicables'
        db_table = 'Normas Aplicables'
        ordering = ['-id']


class Dimensiones(models.Model):
    """Modelo de las dimesniones"""

    caracteristicas_control = models.CharField(
        max_length=255,
        verbose_name='Dimensión'
    )

    unidad_medida = models.CharField(
        max_length=255,
        verbose_name='Unidad de medida'
    )
    
    equipo_medicion = models.CharField(
        max_length=255,
        verbose_name='Equipo de medición'
    )

    def __str__(self):
        return self.caracteristicas_control

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Dimensión'
        verbose_name_plural = 'Dimensiones'
        db_table = 'Dimensiones'
        ordering = ['-id']


class Pruebas(models.Model):
    """Modelo de las pruebas"""

    variables = models.CharField(
        max_length=255,
        verbose_name='Variables'
    )
    descripcion_prueba = models.CharField(
        max_length=255,
        verbose_name='Descripción de la prueba'
    )
    medio_control = models.CharField(
        max_length=255,
        verbose_name='Medio de control'
    )

    def __str__(self):
        return self.variables

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'
        db_table = 'Pruebas'
        ordering = ['-id']


class Atributos(models.Model):
    """Modelos de atributos"""

    caracteristicas = models.CharField(
        max_length=255,
        verbose_name='Caracteristicas'
    )

    especificacion = models.CharField(
        max_length=255,
        verbose_name='Especificación'
    )
    
    observacion = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Observaciones'
    )

    def __str__(self):
        return self.caracteristicas

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'
        db_table = 'Atributos'
        ordering = ['-id']


class Normas(models.Model):
    """Modelo de las normas"""


    codigo = models.CharField(
        max_length=255,
        verbose_name='Código'
    )
    titulo = models.CharField(
        max_length=255,
        verbose_name='Titulo'
    )

    def __str__(self):
        return self.titulo

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Norma'
        verbose_name_plural = 'Normas'
        db_table = 'Normas'
        ordering = ['-id']
