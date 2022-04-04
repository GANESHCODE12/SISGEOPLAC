"""Modelos de Producción"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user

#Modelos
from users.models import User
from Control_produccion.models import ControlProduccion


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
        'Productos.Producto',
        on_delete=models.CASCADE,
        verbose_name='Nombre del Producto',
    )

    lote = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Lote'
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

    maquina = models.CharField(
        max_length=40,
        blank=True,
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

    color = models.CharField(
        max_length=30,
        verbose_name='Color'
    )
    referencia_pigmento = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Referencia pigmento'
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

        cantidad = (self.producto.cavidades)/self.producto.ciclo

        return cantidad * 28800

    @property
    def numero_cajas(self):
        """Retorna el número de cajas"""

        return self.cantidad_requerida/self.producto.unidad_empaque

    @property
    def cantidad_mpkg(self):
        """Retorna la materia prima en Kg"""

        cantidad = self.producto.peso * self.cantidad_requerida

        return cantidad / 1000

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Produccion'
        verbose_name_plural = 'Ordenes de produccion'
        db_table = 'Ordenes de producción'
        ordering = ['-numero_op']
