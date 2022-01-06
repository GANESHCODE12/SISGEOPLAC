"""Modelo para el listado maestro de documentos"""

#Django
from django.db import models
from django.forms import model_to_dict

#Utilidades
from crum import get_current_user

#Modelos
from users.models import User


class Documentacion(models.Model):
    """Modelos de listado maestro de documentos"""

    creado_por = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='creado_por'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    actualizado_por = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='actualizado_por',
        null=True,
        blank=True,
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    
    lista_tipo_documento = [
        ('Procedimiento','Procedimiento'),
        ('Instructivo','Instructivo'),
        ('Formato','Formato'),
        ('Matriz','Matriz'),
        ('Plan','Plan'),
        ('Manual','Manual'),
        ('Politica','Politica'),
        ('Programa','Programa'),
        ('Documento externo','Documento externo'),
        ('Norma','Norma'),
    ]
    tipo_documento = models.CharField(
        max_length=50,
        choices=lista_tipo_documento,
        verbose_name='Tipo de documento'
    )
    
    proceso = models.CharField(
        max_length=100,
        verbose_name='Proceso'
    )

    codigo = models.CharField(
        max_length=20,
        verbose_name='Código'
    )

    titulo = models.CharField(
        max_length=100,
        verbose_name='Titulo'
    )

    versión = models.PositiveIntegerField(
        verbose_name='Versión'
    )

    fecha = models.DateField(
        verbose_name='Fecha de vigencia'
    )

    ubicacion = models.CharField(
        max_length=50,
        verbose_name='Ubicación'
    )

    lista_medio_almacenamiento = [
        ('Físico','Físico'),
        ('Digital','Digital'),
    ]
    medio_almacenamiento = models.CharField(
        max_length=20,
        choices=lista_medio_almacenamiento,
        verbose_name='Medio de almacenamiento'
    )

    lista_estado_documento = [
        ('Vigente','Vigente'),
        ('Obsoleto','Obsoleto'),
        ('En elaboración','En elaboración'),
        ('En aprobación','En aprobación'),
        ('En revisión','En revisión'),
    ]
    estado_documento = models.CharField(
        max_length=40,
        choices=lista_estado_documento,
        verbose_name='Estado del documento'
    )

    si_no = [
        ('Si','Si'),
        ('No','No'),
    ]

    se_trasnforma_registro = models.CharField(
        max_length=7,
        choices=si_no,
        verbose_name='Se transforma en registro?'
    )

    dependencia_lider = models.CharField(
        max_length=80,
        verbose_name='Dependencia lider'
    )

    control_cambios = models.TextField(
        blank=True,
        verbose_name='Control de cambios'
    )

    documento = models.FileField(
        upload_to='Documentación/Documentos',
        verbose_name='Documento'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.creado_por = user
            else:
                self.actualizado_por = user
        return super(Documentacion, self).save()

    def __str__(self):
        return self.titulo

    def toJSON(self):
        item = model_to_dict(
            self,
            exclude=[
                'documento'
            ]
        )
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        db_table = 'Documentos'
        ordering = ['-id']
