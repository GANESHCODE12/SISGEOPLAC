"""Modelos para inspecciones de calidad"""

#Django
from django.db import models
from django.forms import model_to_dict

#Modelos
from users.models import User

#Utilidades
from crum import get_current_user


class ControlCalidad(models.Model):
    """Modelo con información general de las
    inspecciones de calidad"""

    inspector = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    inspector_actualizo = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_actualizo',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    
    numero_op = models.ForeignKey(
        'Produccion.Produccion',
        on_delete=models.CASCADE,
        verbose_name='Número de orden',
    )

    tecnico = models.CharField(
        max_length=30,
        verbose_name='Técnico',
    )

    operario = models.CharField(
        max_length=30,
        verbose_name='Operario'
    )

    lista_turno = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]

    turno = models.CharField(
        max_length=10,
        choices=lista_turno,
        default='1',
        verbose_name='Turno'
    )

    fecha_despacho = models.DateField(
        null=True,
        verbose_name='Fecha despacho',
    )

    cantidad_solicitada = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad solicitada'
    )
    
    empaque_y_embalaje = models.TextField(
        blank=True,
        verbose_name='Empaque y embalaje'
    )

    observaciones = models.TextField(
        blank=True,
        verbose_name='Observaciones'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector = user
            else:
                self.inspector_actualizo = user
        return super(ControlCalidad, self).save()

    def __str__(self):
        return 'Inspección a orden {}'.format(self.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    @property
    def saldo_cliente(self):
        """Función que retorna el saldo pendiente de despachar
        al cliente"""

        return(self.numero_op.cantidad_requerida - self.cantidad_solicitada)

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspección de calidad'
        verbose_name_plural = 'Inspecciones de calidad'
        db_table = 'Inspecciones de calidad'
        ordering = ['-id']


class PruebasCalidad(models.Model):
    """Modelo de resultado de las pruebas realizadas"""

    inspector_p = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_p'
    )

    fecha_creacion_p = models.DateTimeField(
        auto_now_add=True,
    )

    inspector_actualizo_p = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_actualizo_p',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion_p = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_inspeccion_p = models.ForeignKey(
        'Control_calidad.ControlCalidad',
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
    )

    pruebas_y_o_ensayos = models.ForeignKey(
        'Productos.PruebasEnsayo',
        on_delete = models.CASCADE,
        verbose_name='Pruebas y/o ensayos',
    )

    metodo_p = models.CharField(
        max_length=40,
        verbose_name='Método'
    )

    resultado_p = models.CharField(
        max_length=30,
        verbose_name='Resultado'
    )

    valor = models.FloatField(
        verbose_name='Valor'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_p = user
            else:
                self.inspector_actualizo_p = user
        return super(PruebasCalidad, self).save()

    def __str__(self):
        return '{} de la orden {}'.format(self.pruebas_y_o_ensayos, self.id_inspeccion_p.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspeccion a prueba'
        verbose_name_plural = 'Inspecciones a pruebas'
        db_table = 'Inspecciones a pruebas'
        ordering = ['-id']


class InspeccionAtributos(models.Model):
    """Modelo de inspección por atributos"""

    inspector_a = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_a'
    )

    fecha_creacion_a = models.DateTimeField(
        auto_now_add=True,
    )

    inspector_actualizo_a = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_actualizo_a',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion_a = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_inspeccion_a = models.ForeignKey(
        'Control_calidad.ControlCalidad',
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
    )

    inspeccion_atributos = models.ForeignKey(
        'Productos.ControlAtributo',
        on_delete=models.CASCADE,
        verbose_name='Atributos',
    )

    resultado_ia = models.CharField(
        max_length=30,
        verbose_name='Resultado'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_a = user
            else:
                self.inspector_actualizo_a = user
        return super(InspeccionAtributos, self).save()

    def __str__(self):
        return '{} de la orden {}'.format(self.inspeccion_atributos, self.id_inspeccion_a.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspección a atributo'
        verbose_name_plural = 'Inspecciones a atributos'
        db_table = 'Inspecciones a atributos'
        ordering = ['-id']


class InspeccionDimensional(models.Model):
    """Modelo de inspección dimensional realizado al producto"""

    inspector_d = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_d'
    )

    fecha_creacion_d = models.DateTimeField(
        auto_now_add=True,
    )

    inspector_actualizo_d = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_actualizo_d',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion_d = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    id_inspeccion_d = models.ForeignKey(
        'Control_calidad.ControlCalidad',
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
    )

    inspeccion_dimensional = models.ForeignKey(
        'Productos.CaracteristicasDimensionale',
        on_delete=models.CASCADE,
        verbose_name='Dimensión',
    )

    promedio = models.FloatField(
        verbose_name='Promedio'
    )

    resultado_id = models.CharField(
        max_length=30,
        verbose_name='Resultado'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_d = user
            else:
                self.inspector_actualizo_d = user
        return super(InspeccionDimensional, self).save()

    def __str__(self):
        return '{} de la orden {}'.format(self.inspeccion_dimensional, self.id_inspeccion_d.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspección a dimensiones'
        verbose_name_plural = 'Inspecciones a dimensiones'
        db_table = 'Inspecciones a dimensiones'
        ordering = ['-id']

