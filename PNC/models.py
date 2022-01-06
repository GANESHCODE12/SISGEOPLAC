"""Model definition for Nonconforming product database"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user

#Modelos
from users.models import User


class ProductoNoConforme(models.Model):
    """Modelo de producto no conforme"""

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


    """Para agregar un tipo de producto no conforme se debe modificar la siguiente lista"""

    lista_tipo_pnc = [
        ('LINER INCOMPLETO','LINER INCOMPLETO'),
        ('ORIFICIO TAPADO','ORIFICIO TAPADO'),
        ('ROSCA DEFECTUOSA','ROSCA DEFECTUOSA'),
        ('PANDEAMIENTO','PANDEAMIENTO'),
        ('FUERA DE MEDIDAS','FUERA DE MEDIDAS'),
        ('CONTAMINACIÓN','CONTAMINACIÓN'),
        ('MANCHAS','MANCHAS'),
        ('PIEZA INCOMPLETA','PIEZA INCOMPLETA'),
        ('REBABAS','REBABAS'),
        ('FUERA DE COLOR','FUERA DE COLOR'),
        ('RECHUPE','RECHUPE'),
        ('PERFORACIONES','PERFORACIONES'),
        ('FUERA DE PESO','FUERA DE PESO'),
        ('EMBUTIDO','EMBUTIDO'),
        ('PEGOTES','PEGOTES'),
        ('BOCA MAL FORMADA','BOCA MAL FORMADA'),
        ('POROSIDAD','POROSIDAD'),
        ('RAYAS','RAYAS'),
        ('DESCALIBRE','DESCALIBRE'),
        ('CUELLO INCLINADO','CUELLO INCLINADO'),
        ('PIEZA CON GRASA','PIEZA CON GRASA'),
        ('FILTRACIÓN DE AGUA','FILTRACIÓN DE AGUA'),
        ('ENVASES PEGADOS AL MOLDE','ENVASES PEGADOS AL MOLDE'),
        ('PARTICULAS EXTRAÑAS','PARTICULAS EXTRAÑAS'),
        ('OTROS','OTROS'), 
    ]

    tipo_pnc_1 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        verbose_name='Tipo PNC 1'
    )
    tipo_pnc_2 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 2'
    )
    tipo_pnc_3 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 3'
    )
    tipo_pnc_4 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 4'
    )
    tipo_pnc_5 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 5'
    )
    tipo_pnc_6 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 6'
    )
    tipo_pnc_7 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 7'
    )
    tipo_pnc_8 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 8'
    )
    tipo_pnc_9 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 9'
    )
    tipo_pnc_10 = models.CharField(
        max_length=60,
        choices=lista_tipo_pnc,
        blank=True,
        verbose_name='Tipo PNC 10'
    )

    lista_estado_pnc = [
        ('Liberado', 'Liberado'),
        ('Destruido', 'Destruido'),
        ('Conciliado', 'Conciliado'),
        ('Pendiente', 'Pendiente'),
    ]
    estado_pnc = models.CharField(
        max_length=30,
        choices=lista_estado_pnc,
        default='Pendiente',
        verbose_name='Estado PNC'
    )

    cantidad_pnc = models.PositiveIntegerField(
        verbose_name='Cantidad PNC'
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