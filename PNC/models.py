"""Model definition for Nonconforming product database"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user

#Modelos
from users.models import User


class MotivoPnc(models.Model):

    motivo = models.CharField(
        max_length=100,
        verbose_name="Motivo producto no conforme"
    )

    def __str__(self):
        return self.motivo

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Motivo producto no conforme'
        verbose_name_plural = 'Motivos productos no conformes'
        db_table = 'Motivos productos no conformes'
        ordering = ['-id']


class ProductoNoConforme(models.Model):

    inspector_calidad = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )
    inspector_calidad_actualiza = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad_actualiza',
        null=True,
        blank=True,
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    id_inspeccion = models.ForeignKey(
        'Control_calidad.ControlCalidad', 
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
    )
    tipo_pnc = models.ForeignKey(
        MotivoPnc,
        on_delete=models.CASCADE,
        verbose_name='Tipo PNC',
        null=True,
        blank=True
    )
    estado_pnc = models.CharField(
        max_length=30,
        default='Pendiente',
        verbose_name='Estado PNC'
    )
    cantidad_pnc = models.PositiveIntegerField(
        verbose_name='Cantidad PNC'
    )
    tecnico = models.CharField(
        max_length=100,
        verbose_name='Técnico',
        blank=True,
        null=True
    )
    operario_1 = models.CharField(
        max_length=100,
        verbose_name='Operario 1',
        blank=True,
        null=True
    )
    operario_2 = models.CharField(
        max_length=100,
        verbose_name='Operario 2',
        blank=True,
        null=True
    )
    operario_3 = models.CharField(
        max_length=100,
        verbose_name='Operario 3',
        blank=True,
        null=True
    )
    observaciones = models.TextField(
        blank=True,
        verbose_name='Observaciones'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_calidad = user
            else:
                self.inspector_calidad_actualiza = user
        return super(ProductoNoConforme, self).save()

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Producto no conforme'
        verbose_name_plural = 'Productos no conformes'
        db_table = 'Productos no conformes'
        ordering = ['-id']


class TrazabilidadProductoNoConforme(models.Model):

    inspector_calidad = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad_trazabilidad'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )
    inspector_calidad_actualiza = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad_actualiza_trazabilidad',
        null=True,
        blank=True,
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    id_inspeccion = models.ForeignKey(
        'Control_calidad.ControlCalidad', 
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
        related_name='inspeccion_trazabilidad',
    )
    tipo_pnc = models.ForeignKey(
        MotivoPnc,
        on_delete=models.CASCADE,
        verbose_name='Tipo PNC',
        related_name='tipo_pnc_trazabilidad',
        null=True,
        blank=True
    )
    estado_pnc = models.CharField(
        max_length=30,
        default='Pendiente',
        verbose_name='Estado PNC'
    )
    cantidad_pnc = models.PositiveIntegerField(
        verbose_name='Cantidad PNC'
    )
    tecnico = models.CharField(
        max_length=100,
        verbose_name='Técnico',
        blank=True,
        null=True
    )
    operario_1 = models.CharField(
        max_length=100,
        verbose_name='Operario 1',
        blank=True,
        null=True
    )
    operario_2 = models.CharField(
        max_length=100,
        verbose_name='Operario 2',
        blank=True,
        null=True
    )
    operario_3 = models.CharField(
        max_length=100,
        verbose_name='Operario 3',
        blank=True,
        null=True
    )
    observaciones = models.TextField(
        blank=True,
        verbose_name='Observaciones'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_calidad = user
            else:
                self.inspector_calidad_actualiza = user
        return super(TrazabilidadProductoNoConforme, self).save()

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Producto no conforme'
        verbose_name_plural = 'Productos no conformes'
        db_table = 'Productos no conformes'
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Trazabilidad producto no conforme'
        verbose_name_plural = 'Trazabilidad productos no conformes'
        db_table = 'Trazabilidad productos no conformes'
        ordering = ['-id']
