"""Modelos de Producción"""

#Django
from django.db import models
from django.forms import model_to_dict
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

#Utilidades
from crum import get_current_user

# signals
from notify.signals import notificar

#Modelos
from users.models import User


class Produccion(models.Model):
    """Modelo de orden de producción"""

    usuario = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='usuario'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )
    usuario_actualizo = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='ususario_actualizo',
        null=True,
        blank=True,
    )  
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    numero_op = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        verbose_name='Número de orden'
    )
    producto = models.ForeignKey(
        'Productos.Productos_colores',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto',
    )  
    orden_compra = models.CharField(
        max_length=40,
        verbose_name='Orden de compra'
    )
    cliente = models.CharField(
        max_length=100,
        verbose_name='Cliente'
    )
    cantidad_requerida = models.PositiveIntegerField(
        verbose_name='Cantidad requerida'
    )
    materia_prima_adicional = models.PositiveIntegerField(
        verbose_name='Materia prima adicional',
        null=True,
        blank=True
    )
    pigmento_adicional = models.PositiveIntegerField(
        verbose_name='Cantidad adicional',
        null=True,
        blank=True
    )
    aprobacion_orden = models.BooleanField(
        verbose_name="Aprobación orden",
        default=False
    )
    aprobacion_materia_prima = models.BooleanField(
        verbose_name="Aprobación materia prima",
        default=False
    )
    aprobacion_pigmento = models.BooleanField(
        verbose_name="Aprobación pigmento",
        default=False
    )
    lista_maquina = [
        ('', ''),
        ('Sin asignar', 'Sin asignar'),
        ('Inyectora 1','Inyectora 1'),
        ('Inyectora 2','Inyectora 2'),
        ('Inyectora 3','Inyectora 3'),
        ('Inyectora 4','Inyectora 4'),
        ('Inyectora 5','Inyectora 5'),
        ('Inyectora 6','Inyectora 6'),
        ('Sopladora 1','Sopladora 1'),
        ('Sopladora 2','Sopladora 2'),
        ('Sopladora 3','Sopladora 3'),
        ('Maquila','Maquila'),
        ('Ensable','Ensable'),
    ]
    maquina = models.CharField(
        max_length=40,
        choices=lista_maquina,
        default='',
        verbose_name='Máquina'
    )
    """Para agregar un nuevo estado, modifique la siguiente lista"""
    lista_estado_op = [
        ('En espera','En espera'),
        ('Detenida','Detenida'),
        ('En producción','En producción'),
        ('Terminada','Terminada'),
        ('Rechazada','Rechazada'),
        ('En proceso','En reproceso'),
    ]
    estado_op = models.CharField(
        max_length=30, 
        choices=lista_estado_op,
        default='En espera',
        verbose_name='Estado de la orden'
    )
    fecha_entrega = models.DateField(
        verbose_name='Fecha de entrega'
    )
    observaciones = models.TextField(
        max_length=800, 
        blank=True,
        verbose_name='Observaciones'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.usuario_actualizo = user
        return super(Produccion, self).save()

    def __str__(self):
        return str(self.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    @property
    def cantidad_planeada(self):
        """Retorna la cantidad planeada por turno"""
        cantidad = (self.producto.productos.cavidades)/self.producto.productos.ciclo
        cantidad_real_esperada = cantidad * 28800
        return cantidad_real_esperada

    @property
    def numero_cajas(self):
        """Retorna el número de cajas"""
        return self.cantidad_requerida/self.producto.productos.unidad_empaque

    @property
    def cantidad_mpkg(self):
        """Retorna la materia prima en Kg"""
        cantidad = self.producto.productos.peso * self.cantidad_requerida
        return cantidad / 1000

    @property
    def merma(self):
        merma = self.cantidad_mpkg * 0.03
        return merma

    @property
    def cantidad_maxima(self):
        cantidad_maxima = self.cantidad_mpkg + self.merma
        return cantidad_maxima

    @property
    def maximo_pigmento(self):
        maximo_pigmento = self.cantidad_maxima * 0.02
        return maximo_pigmento

    @property
    def maximo_material(self):
        maximo_material = self.cantidad_maxima * 0.98
        return maximo_material
    
    #incluir en master
    @property
    def tiempo_esperado(self):
        merma_tiempo = (3600 * self.producto.productos.cavidades)/self.producto.productos.ciclo
        tiempo_esperado = (self.cantidad_requerida/merma_tiempo) * 1.1
        return tiempo_esperado

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Produccion'
        verbose_name_plural = 'Ordenes de produccion'
        db_table = 'Ordenes de producción'
        ordering = ['-numero_op']


@receiver(post_save, sender=Produccion)
def notify_production(sender, instance, created, *args, **kwargs):
    if created:
        notificar.send(
            instance.usuario,
            destiny=Group.objects.get(name="Ordenes producción"),  
            verb=instance.numero_op, 
            level='success'
        )
    elif not created and instance.usuario_actualizo != instance.usuario:
        notificar.send(
            instance.usuario_actualizo,
            destiny=Group.objects.get(name="Ordenes producción"),
            verb=instance.numero_op, 
            level='info'
        )


class Desarrollo(models.Model):

    desarrollo_creado_por = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='desarrollo_creado_por'
    )
    fecha_creacion_desarrollo = models.DateTimeField(
        auto_now_add=True,
    )
    usuario_actualizo_desarrollo = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='ususario_actualizo_desarrollo',
        null=True,
        blank=True,
    )  
    fecha_actualizacion_desarrollo = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    producto = models.CharField(
        max_length=200,
        verbose_name="Producto"
    )
    ciclo = models.PositiveBigIntegerField(
        verbose_name='Ciclo'
    )
    solicitado_por = models.CharField(
        max_length=40,
        verbose_name='Solicitado por'
    )
    maquina = models.CharField(
        max_length=40,
        default='',
        verbose_name='Maquina'
    )
    fecha_limite_entrega = models.DateField(
        verbose_name="Fecha limite de entrega"
    )
    fecha_fabricacion = models.DateField(
        verbose_name="Fecha fabricación de las muestras",
        null=True
    )
    cantidad = models.PositiveIntegerField(
        verbose_name='Cantidad'
    )
    tipo_empaque = models.CharField(
        max_length=60,
        verbose_name='Tipo de empaque',
    )
    maquina = models.CharField(
        max_length=40,
        blank=True,
        verbose_name='Máquina'
    )
    objetivo_muestra = models.TextField(
        max_length=800, 
        blank=True,
        verbose_name='Objetivo  muestra'
    )
    seleccion = [
        ('Si','Si'),
        ('No','No'),
        ('No aplica','No aplica'),
    ]
    molde_nuevo = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Molde nuevo?'
    )
    es_funcional = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Es funcional?'
    )
    diseño = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Diseño'
    )
    variables = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Variables'
    )
    peso_solicitado = models.PositiveIntegerField(
        verbose_name='Peso solicitado'
    )
    observaciones = models.TextField(
        max_length=800, 
        blank=True,
        verbose_name='Observaciones'
    )
    color = models.CharField(
        max_length=30, 
        verbose_name='Color'
    )
    cumplimiento = [
        ('Cumple','Cumple'),
        ('No cumple','No cumple'),
        ('No aplica','No aplica'),
    ]
    dimensional = models.CharField(
        max_length=30, 
        choices=cumplimiento,
        default='No aplica',
        verbose_name='Cumple con dimensiones?'
    )
    funcional = models.CharField(
        max_length=30, 
        choices=cumplimiento,
        default='No aplica',
        verbose_name='Cumple con el funcionamiento?'
    )
    atributos = models.CharField(
        max_length=30, 
        choices=cumplimiento,
        default='No aplica',
        verbose_name='Cumple con atributos?'
    )
    muestras = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Requiere más muestras?'
    )
    autorizacion = models.CharField(
        max_length=30, 
        choices=seleccion,
        default='No aplica',
        verbose_name='Requiere autorización?'
    )
    fecha_analisis_muestras = models.DateField(
        verbose_name="Fecha análisis de muestras",
        null=True
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.desarrollo_creado_por = user
            else:
                self.usuario_actualizo_desarrollo = user
        return super(Desarrollo, self).save()

    def __str__(self):
        return 'Producto: {}, solicitud: {}'.format(self.producto, self.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Desarrollo'
        verbose_name_plural = 'Desarrollos'
        db_table = 'Desarrollos'
        ordering = ['-id']


class DesarrolloMuestras(models.Model):
    lista_especificaciones = [
        'Cantidad',
        'Total',
    ]
    desarrollo = models.ForeignKey(
        Desarrollo,
        on_delete=models.CASCADE,
        related_name='desarrollo_muestras'
    )
    mp = models.PositiveBigIntegerField(
        verbose_name='mp'
    )
    pigmentos = models.PositiveBigIntegerField(
        verbose_name='pigmentos'
    )
    empaque = models.PositiveBigIntegerField(
        verbose_name='empaque'
    )
    maquila = models.PositiveBigIntegerField(
        verbose_name='maquila'
    )
    operario = models.PositiveBigIntegerField(
        verbose_name='operario'
    )
    tecnico = models.PositiveBigIntegerField(
        verbose_name='tecnico'
    )
    montaje = models.PositiveBigIntegerField(
        verbose_name='montaje'
    )
    total = models.PositiveBigIntegerField(
        verbose_name='total'
    )

    def __str__(self):
        return 'Inspección: {}'.format(self.desarrollo.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Desarrollo producción'
        verbose_name_plural = 'Desarrollos producción'
        db_table = 'Desarrollos producción'
        ordering = ['-id']
