"""Modelo para el control de la producción"""

#Django
from django.db import models
from django.forms import model_to_dict


#Utilidades
from django.db.models.aggregates import Sum
from crum import get_current_user

#Modelos
from users.models import User


class ControlProduccion(models.Model):
    """Modelo de control de producción"""

    supervisor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='supervisor'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    supervisor_actualizo = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='supervisor_actualizo',
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
        max_length=50,
        verbose_name='Técnico'
    )

    operario = models.CharField(
        max_length=50,
        verbose_name='Operario'
    )

    lista_turno = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    turno = models.CharField(
        max_length=30, 
        choices=lista_turno,
        default='1',
        verbose_name='Turno'
    )

    hora_inicio = models.DateTimeField(
        verbose_name='Hora inicio'
    )

    hora_final = models.DateTimeField(
        verbose_name='Hora Final'
    )

    cantidad_producida = models.PositiveIntegerField(
        verbose_name='Cantidad producida'
    )

    ciclo_turno = models.FloatField(
        verbose_name='Ciclo turno'
    )
    
    cavidades_operacion = models.PositiveIntegerField(
        verbose_name='Cavidades Operación'
    )

    tiempo_paradas = models.DurationField(
        verbose_name='Tiempo de paradas'
    )

    observaciones = models.TextField(
        blank=True,
        verbose_name='Observaciones'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.supervisor = user
            else:
                self.supervisor_actualizo = user
        return super(ControlProduccion, self).save()

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)
        item['saldo_orden'] = self.cantidad_acumulada
        return item

    @property
    def resta_tiempos(self):
        """Retorna la diferencia de tiempo inicio y final de producción"""

        return self.hora_final - self.hora_inicio

    @property
    def tiempo_produccion(self):
        """Retorna el tiempo total de producción"""
    
        resultado = self.resta_tiempos - self.tiempo_paradas

        return resultado

    @property
    def bolsas_completadas(self):
        """Retorna el número de bolsas completadas en 
        el truno"""

        return (self.cantidad_producida / self.numero_op.producto.unidad_empaque)

    @property
    def rendimiento_produccion(self):
        """Retorna en porcentaje el rendimiento de producción"""
        
        return (self.cantidad_producida / (self.numero_op.cantidad_planeada * self.tiempo_produccion.total_seconds())) * 100

    @property
    def cantidad_acumulada(self):
        """Retorna la cantidad acumulada de una orden de producción"""

        pk = self.numero_op
        cantidad = ControlProduccion.objects.filter(numero_op = pk).aggregate(cantidad_acumulada=Sum('cantidad_producida'))

        for self.numero_op.numero_op, value in cantidad.items():
            return value

    @property
    def saldo_orden(self):
        """Función que retorna el saldo pendiente para cerrar 
        la orden"""

        pk = self.numero_op_id
        cantidad = ControlProduccion.objects.filter(numero_op = pk).aggregate(saldo_orden=Sum('cantidad_producida'))

        for self.numero_op.numero_op, value in cantidad.items():
            return self.numero_op.cantidad_requerida  - value

    
    @property
    def cantidad_esperada_turno(self):
        """Retorna la cantida esperada por turno"""

        cantidad = (self.numero_op.producto.cavidades / self.numero_op.producto.ciclo)

        return cantidad * self.tiempo_produccion.total_seconds()
        
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Control orden'
        verbose_name_plural = 'Controles de produccion'
        db_table = 'Controles de produccion'
        ordering = ['-id']