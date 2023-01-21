"""Modelo para el control de la producción"""

#Django
from django.db import models
from django.forms import model_to_dict


#Utilidades
from django.db.models.aggregates import Sum
from crum import get_current_user
from datetime import timedelta

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
        verbose_name='Hora inicio',
        null=True
    )
    hora_final = models.DateTimeField(
        verbose_name='Hora Final',
        null=True
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
    def bolsas_completadas(self):
        """Retorna el número de bolsas completadas en 
        el truno"""

        return (self.cantidad_producida / self.numero_op.producto.productos.unidad_empaque)

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
    def tiempo_total_paradas(self):
        """Retorna el tiempo total de paradas"""

        horas = 0
        minutos = 0
        paradas = TiemposParadasControlProduccion.objects.filter(control_id=self.id)

        for parada in paradas:
            horas += parada.horas
            minutos += parada.minutos
    
        tiempo_total_paradas = timedelta(hours=horas, minutes=minutos)
        return tiempo_total_paradas

    @property
    def tiempo_produccion(self):
        """Retorna el tiempo total de producción"""
    
        resultado = self.resta_tiempos - self.tiempo_total_paradas

        return resultado

    @property
    def cantidad_esperada_turno(self):
        """Retorna la cantida esperada por turno"""

        cantidad = (self.numero_op.producto.productos.cavidades / self.numero_op.producto.productos.ciclo)

        return cantidad * self.tiempo_produccion.total_seconds()

    @property
    def rendimiento_produccion(self):
        """Retorna en porcentaje el rendimiento de producción"""
        
        return (
            self.cantidad_producida / self.cantidad_esperada_turno
        ) * 100
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Control orden'
        verbose_name_plural = 'Controles de produccion'
        db_table = 'Controles de produccion'
        ordering = ['-id']


class ColaboradorControlProduccion(models.Model):
    """Modelo colaboradores en control de producción"""

    control = models.ForeignKey(
        ControlProduccion,
        on_delete = models.CASCADE,
        related_name='Control'
    )
    colaborador = models.ForeignKey(
        'Gestion_Humana.TecnicosOperarios',
        on_delete=models.CASCADE,
        verbose_name='Colaborador',
    )

    def __str__(self):
        return 'Control Producción: {}, Colaborador: {}'.format(self.control, self.colaborador.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['control'] = self.controlproduccion_set.all()
        item['colaboradores'] = self.tecnicosoperarios_set.all()
        return item
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Colaborador Control orden'
        verbose_name_plural = 'Colaborador Controles de produccion'
        db_table = 'Colaborador Controles de produccion'
        ordering = ['-id']


class MotivosParadasControlProduccion(models.Model):
    """Modelo de motivos de paradas"""

    motivo = models.CharField(
        max_length=50,
        verbose_name="Motivo Parada",
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'Motivo: {}'.format(self.motivo)

    def toJSON(self):
        item = model_to_dict(self)
        return item  
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Motivo de parada'
        verbose_name_plural = 'Motivos de paradas'
        db_table = 'Motivos de paradas'
        ordering = ['-id']


class TiemposParadasControlProduccion(models.Model):
    """Modelo de tiempos de paradas"""

    control = models.ForeignKey(
        ControlProduccion,
        on_delete = models.CASCADE,
        related_name='Control_Parada'
    )
    motivo = models.ForeignKey(
        MotivosParadasControlProduccion,
        on_delete = models.CASCADE,
        null=True,
        verbose_name="Motivo Parada",
    )
    horas = models.PositiveBigIntegerField(
        verbose_name="Segundos",
        null=True
    )
    minutos = models.PositiveBigIntegerField(
        verbose_name="Minutos",
        null=True
    )

    def __str__(self):
        return 'Control Producción: {}, Motivo: {}'.format(self.control, self.motivo)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    @property
    def tiempo_paradas(self):
        """Retorna el tiempo de las paradas"""
    
        tiempo = timedelta(hours=self.horas, minutes=self.minutos)
        return tiempo
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Tiempo de parada'
        verbose_name_plural = 'Tiempos de paradas'
        db_table = 'Tiempos de paradas'
        ordering = ['-id']
