"""Modelos para inspecciones de calidad"""

#Django
from django.db import models
from django.forms import model_to_dict

#Modelos
from users.models import User
from Inventario.models import Entrada

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
    lista_turno = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    turno = models.CharField(
        max_length=10,
        choices=lista_turno,
        default='1',
        verbose_name='Turno'
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
    cavidad_1 = models.FloatField(
        verbose_name='cavidad_1',
        blank=True,
        null=True,
    )
    cavidad_2 = models.FloatField(
        verbose_name='cavidad_2',
        blank=True,
        null=True,
    )
    cavidad_3 = models.FloatField(
        verbose_name='cavidad_3',
        blank=True,
        null=True,
    )
    cavidad_4 = models.FloatField(
        verbose_name='cavidad_4',
        blank=True,
        null=True,
    )
    cavidad_5 = models.FloatField(
        verbose_name='cavidad_5',
        blank=True,
        null=True,
    )
    cavidad_6 = models.FloatField(
        verbose_name='cavidad_6',
        blank=True,
        null=True,
    )
    cavidad_7 = models.FloatField(
        verbose_name='cavidad_7',
        blank=True,
        null=True,
    )
    cavidad_8 = models.FloatField(
        verbose_name='cavidad_8',
        blank=True,
        null=True,
    )
    cavidad_9 = models.FloatField(
        verbose_name='cavidad_9',
        blank=True,
        null=True,
    )
    cavidad_10 = models.FloatField(
        verbose_name='cavidad_10',
        blank=True,
        null=True,
    )
    cavidad_11 = models.FloatField(
        verbose_name='cavidad_11',
        blank=True,
        null=True,
    )
    cavidad_12 = models.FloatField(
        verbose_name='cavidad_12',
        blank=True,
        null=True,
    )
    cavidad_13 = models.FloatField(
        verbose_name='cavidad_13',
        blank=True,
        null=True,
    )
    cavidad_14 = models.FloatField(
        verbose_name='cavidad_14',
        blank=True,
        null=True,
    )
    cavidad_15 = models.FloatField(
        verbose_name='cavidad_15',
        blank=True,
        null=True,
    )
    cavidad_16 = models.FloatField(
        verbose_name='cavidad_16',
        blank=True,
        null=True,
    )
    cavidad_17 = models.FloatField(
        verbose_name='cavidad_17',
        blank=True,
        null=True,
    )
    cavidad_18 = models.FloatField(
        verbose_name='cavidad_18',
        blank=True,
        null=True,
    )
    cavidad_19 = models.FloatField(
        verbose_name='cavidad_19',
        blank=True,
        null=True,
    )
    cavidad_20 = models.FloatField(
        verbose_name='cavidad_20',
        blank=True,
        null=True,
    )
    cavidad_21 = models.FloatField(
        verbose_name='cavidad_21',
        blank=True,
        null=True,
    )
    cavidad_22 = models.FloatField(
        verbose_name='cavidad_22',
        blank=True,
        null=True,
    )
    cavidad_23 = models.FloatField(
        verbose_name='cavidad_23',
        blank=True,
        null=True,
    )
    cavidad_24 = models.FloatField(
        verbose_name='cavidad_24',
        blank=True,
        null=True,
    )
    cavidad_25 = models.FloatField(
        verbose_name='cavidad_25',
        blank=True,
        null=True,
    )
    cavidad_26 = models.FloatField(
        verbose_name='cavidad_26',
        blank=True,
        null=True,
    )
    cavidad_27 = models.FloatField(
        verbose_name='cavidad_27',
        blank=True,
        null=True,
    )
    cavidad_28 = models.FloatField(
        verbose_name='cavidad_28',
        blank=True,
        null=True,
    )
    cavidad_29 = models.FloatField(
        verbose_name='cavidad_29',
        blank=True,
        null=True,
    )
    cavidad_30 = models.FloatField(
        verbose_name='cavidad_30',
        blank=True,
        null=True,
    )
    cavidad_31 = models.FloatField(
        verbose_name='cavidad_31',
        blank=True,
        null=True,
    )
    cavidad_32 = models.FloatField(
        verbose_name='cavidad_32',
        blank=True,
        null=True,
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
    cavidad_1 = models.FloatField(
        verbose_name='cavidad_1',
        blank=True,
        null=True,
    )
    cavidad_2 = models.FloatField(
        verbose_name='cavidad_2',
        blank=True,
        null=True,
    )
    cavidad_3 = models.FloatField(
        verbose_name='cavidad_3',
        blank=True,
        null=True,
    )
    cavidad_4 = models.FloatField(
        verbose_name='cavidad_4',
        blank=True,
        null=True,
    )
    cavidad_5 = models.FloatField(
        verbose_name='cavidad_5',
        blank=True,
        null=True,
    )
    cavidad_6 = models.FloatField(
        verbose_name='cavidad_6',
        blank=True,
        null=True,
    )
    cavidad_7 = models.FloatField(
        verbose_name='cavidad_7',
        blank=True,
        null=True,
    )
    cavidad_8 = models.FloatField(
        verbose_name='cavidad_8',
        blank=True,
        null=True,
    )
    cavidad_9 = models.FloatField(
        verbose_name='cavidad_9',
        blank=True,
        null=True,
    )
    cavidad_10 = models.FloatField(
        verbose_name='cavidad_10',
        blank=True,
        null=True,
    )
    cavidad_11 = models.FloatField(
        verbose_name='cavidad_11',
        blank=True,
        null=True,
    )
    cavidad_12 = models.FloatField(
        verbose_name='cavidad_12',
        blank=True,
        null=True,
    )
    cavidad_13 = models.FloatField(
        verbose_name='cavidad_13',
        blank=True,
        null=True,
    )
    cavidad_14 = models.FloatField(
        verbose_name='cavidad_14',
        blank=True,
        null=True,
    )
    cavidad_15 = models.FloatField(
        verbose_name='cavidad_15',
        blank=True,
        null=True,
    )
    cavidad_16 = models.FloatField(
        verbose_name='cavidad_16',
        blank=True,
        null=True,
    )
    cavidad_17 = models.FloatField(
        verbose_name='cavidad_17',
        blank=True,
        null=True,
    )
    cavidad_18 = models.FloatField(
        verbose_name='cavidad_18',
        blank=True,
        null=True,
    )
    cavidad_19 = models.FloatField(
        verbose_name='cavidad_19',
        blank=True,
        null=True,
    )
    cavidad_20 = models.FloatField(
        verbose_name='cavidad_20',
        blank=True,
        null=True,
    )
    cavidad_21 = models.FloatField(
        verbose_name='cavidad_21',
        blank=True,
        null=True,
    )
    cavidad_22 = models.FloatField(
        verbose_name='cavidad_22',
        blank=True,
        null=True,
    )
    cavidad_23 = models.FloatField(
        verbose_name='cavidad_23',
        blank=True,
        null=True,
    )
    cavidad_24 = models.FloatField(
        verbose_name='cavidad_24',
        blank=True,
        null=True,
    )
    cavidad_25 = models.FloatField(
        verbose_name='cavidad_25',
        blank=True,
        null=True,
    )
    cavidad_26 = models.FloatField(
        verbose_name='cavidad_26',
        blank=True,
        null=True,
    )
    cavidad_27 = models.FloatField(
        verbose_name='cavidad_27',
        blank=True,
        null=True,
    )
    cavidad_28 = models.FloatField(
        verbose_name='cavidad_28',
        blank=True,
        null=True,
    )
    cavidad_29 = models.FloatField(
        verbose_name='cavidad_29',
        blank=True,
        null=True,
    )
    cavidad_30 = models.FloatField(
        verbose_name='cavidad_30',
        blank=True,
        null=True,
    )
    cavidad_31 = models.FloatField(
        verbose_name='cavidad_31',
        blank=True,
        null=True,
    )
    cavidad_32 = models.FloatField(
        verbose_name='cavidad_32',
        blank=True,
        null=True,
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


class ColaboradorInspeccionCalidad(models.Model):
    """Modelo colaboradores en inspecciones de calidad"""

    inspeccion = models.ForeignKey(
        ControlCalidad,
        on_delete = models.CASCADE,
        related_name='Control'
    )
    colaborador = models.ForeignKey(
        'Gestion_Humana.TecnicosOperarios',
        on_delete=models.CASCADE,
        verbose_name='Colaborador',
    )

    def __str__(self):
        return 'Control Producción: {}, Colaborador: {}'.format(self.inspeccion, self.colaborador.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item
        
    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Colaborador Inspección Calidad'
        verbose_name_plural = 'Colaboradores Inpección Calidad'
        db_table = 'Colaboradores Inpección Calidad'
        ordering = ['-id']


class CertificadosCalidad(models.Model):
    """Modelo de certificados de calidad"""

    generado_por = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='generado_por'
    )
    fecha_generacion = models.DateTimeField(
        auto_now_add=True,
    )
    certificado_actualizado_por = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='certificado_actualizado_por',
        null=True,
        blank=True,
    )
    fecha_actualizacion_certificado = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    inspeccion_certificado = models.ForeignKey(
        ControlCalidad,
        on_delete=models.CASCADE,
        verbose_name='Número de inspección',
        related_name='certificado_calidad'
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
    cliente_despacho =models.CharField(
        blank=True,
        verbose_name='Cliente Despacho',
        null=True,
        max_length=30
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.generado_por = user
            else:
                self.certificado_actualizado_por = user
        return super(CertificadosCalidad, self).save()

    def __str__(self):
        return 'Inspección a orden {}'.format(self.inspeccion_certificado.numero_op)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Certificado de calidad'
        verbose_name_plural = 'Certificados de calidad'
        db_table = 'Certificados de calidad'
        ordering = ['-id']


class NivelDeInspeccion(models.Model):
    """Modelo de nivel de inspección"""

    inspeccion_calidad = models.ForeignKey(
        ControlCalidad,
        on_delete=models.CASCADE,
        verbose_name='Inspección Calidad',
        related_name='inspeccion_calidad'
    )
    lista_tipo_nivel = [
        ('Niveles especiales de inspección','Niveles especiales de inspección'),
        ('Niveles normales de inspección','Niveles normales de inspección'),
    ]
    tipo_nivel = models.CharField(
        max_length=100,
        choices=lista_tipo_nivel,
        default='1',
        verbose_name='Tipo Nivel'
    )
    lista_codigo_nivel = [
        ('S-1','S-1'),
        ('S-2','S-1'),
        ('S-3','S-1'),
        ('S-4','S-1'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    codigo_nivel = models.CharField(
        max_length=10,
        choices=lista_codigo_nivel,
        default='S-1',
        verbose_name='Código Nivel'
    )
    cantidades_inspeccionar = models.PositiveIntegerField(
        verbose_name='Cantidades a inspeccionar',
        default=0
    )
    letra = models.CharField(
        max_length=5,
        default=''
    )

    def __str__(self):
        return 'Niveles de la inspección: {}'.format(self.inspeccion_calidad)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Nivel de inspección'
        verbose_name_plural = 'Niveles de inspección'
        db_table = 'Niveles de inspección'
        ordering = ['-id']


class MateriaPrimaInsumos(models.Model):
    """Modelo con información general de las
    inspecciones de calidad a la materia prima"""

    inspector_calidad = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad_mp'
    )
    inspector_calidad_actualizo = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='inspector_calidad_actualizo_mp',
        null=True,
        blank=True,
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    materia_prima_insumo = models.ForeignKey(
        Entrada,
        on_delete = models.CASCADE,
        related_name='materia_prima_insumo',
        null=True,
        blank=True,
    )
    arte_cliente = models.CharField(
        max_length=100,
        verbose_name="Arte cliente",
        blank=True,
        null=True
    )
    unidades_muestra = models.PositiveBigIntegerField(
        verbose_name='Cantidad de unidades de muestra'
    )
    unidades_lote = models.PositiveBigIntegerField(
        verbose_name='Cantidad de unidades del lote'
    )
    lote = models.CharField(
        max_length=50,
        default=''
    )
    proveedor = models.CharField(
        max_length=100,
        verbose_name="Proveedor",
        blank=True,
        null=True
    )
    fecha_lote = models.DateField(
        verbose_name='Fecha de fabricación'
    )
    arte_ingreso = models.CharField(
        max_length=100,
        verbose_name="Arte ingreso",
        blank=True,
        null=True
    )
    unidades_empaque = models.PositiveBigIntegerField(
        verbose_name='Cantidad de unidades de empaque revisadas'
    )
    certificado = models.BooleanField(
        verbose_name='Certificado de calidad',
        default=False
    )
    especificaciones = models.BooleanField(
        verbose_name='Cumple especificaciones',
        default=False
    )
    lote_ingreso = models.BooleanField(
        verbose_name='Coincide con lote de ingreso'
    )
    observaciones = models.TextField(
        blank=True,
        verbose_name='Observaciones'
    )
    revisado_por = models.CharField(
        max_length=100,
        verbose_name="Revisado por",
        blank=True,
        null=True
    )
    aprobado = models.BooleanField(
        verbose_name='Aprobado',
        default=False
    )
    tolerado = models.BooleanField(
        verbose_name='Tolerado',
        default=False
    )
    lista_estado = [
        ('Conforme','Conforme'),
        ('Retenido','Retenido'),
        ('En devolución','En devolución'),
        ('Devuelto','Devuelto'),
        ('Conciliado','Conciliado'),
        ('En espera', 'En espera'),
    ]
    estado = models.CharField(
        max_length=40, 
        choices=lista_estado,
        default='En espera',
        verbose_name='Estado del material'
    )

    def save(self, force_insert=False, force_update= False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.inspector_calidad = user
            else:
                self.inspector_calidad_actualizo = user
        return super(MateriaPrimaInsumos, self).save()

    def __str__(self):
        return 'Producto {}, Referencia {}, Lote {}, inspección {}'.format(
            self.materia_prima_insumo.ingreso_materia_prima.nombre,
            self.materia_prima_insumo.ingreso_materia_prima.referencia,
            self.materia_prima_insumo.lote,
            self.id
        )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspección a materia prima e insumos'
        verbose_name_plural = 'Inspecciones a materia prima e insumos'
        db_table = 'Inspección materia prima e insumos'
        ordering = ['-id']


class Analisis(models.Model):

    inspeccion = models.ForeignKey(
        MateriaPrimaInsumos,
        on_delete=models.CASCADE,
        related_name='Analisis',
        null=True,
        blank=True
    )
    especificacion = models.CharField(
        max_length=40,
        verbose_name='Especificación'
    )
    cumple = models.CharField(
        max_length=40,
        verbose_name='Cumple'
    )
    especificacion_list = [
        'Humedad',
        'Paquetes / Bolsas deterioradas',
        'Identificación de Mp / Insumos',
        'Forma de granulo / pellets',
        'Presencia de material extraño',
        'Contaminación volátil',
        'Acople',
        'Lectura código de barras',
        'Hermeticidad',
        'Adherencia',
        'Torque',
        'Prueba de impacto',
    ]

    def __str__(self):
        return 'Producto {}, lote {}, inspección {}'.format(
            self.inspeccion.materia_prima_insumo.ingreso_materia_prima.nombre,
            self.inspeccion.materia_prima_insumo.lote,
            self.inspeccion.id,
        )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Analisis de atributos y funcional'
        verbose_name_plural = 'Analisis de atributos y funcional'
        db_table = 'Analisis de atributos y funcional'
        ordering = ['-id']


class Dimensional(models.Model):

    inspeccion = models.ForeignKey(
        MateriaPrimaInsumos,
        on_delete=models.CASCADE,
        related_name='Analisis_dimensional',
        null=True,
        blank=True
    )
    especificacion = models.CharField(
        max_length=40,
        verbose_name='Especificación',
        null=True,
        blank=True
    )
    muestra_1 = models.FloatField(
        verbose_name='muestra_1',
        blank=True,
        null=True,
    )
    muestra_2 = models.FloatField(
        verbose_name='muestra_2',
        blank=True,
        null=True,
    )
    muestra_3 = models.FloatField(
        verbose_name='muestra_3',
        blank=True,
        null=True,
    )
    muestra_4 = models.FloatField(
        verbose_name='muestra_4',
        blank=True,
        null=True,
    )
    muestra_5 = models.FloatField(
        verbose_name='muestra_5',
        blank=True,
        null=True,
    )
    muestra_6 = models.FloatField(
        verbose_name='muestra_6',
        blank=True,
        null=True,
    )
    muestra_7 = models.FloatField(
        verbose_name='muestra_7',
        blank=True,
        null=True,
    )
    muestra_8 = models.FloatField(
        verbose_name='muestra_8',
        blank=True,
        null=True,
    )
    muestra_9 = models.FloatField(
        verbose_name='muestra_9',
        blank=True,
        null=True,
    )
    muestra_10 = models.FloatField(
        verbose_name='muestra_10',
        blank=True,
        null=True,
    )
    muestra_11 = models.FloatField(
        verbose_name='muestra_11',
        blank=True,
        null=True,
    )
    muestra_12 = models.FloatField(
        verbose_name='muestra_12',
        blank=True,
        null=True,
    )
    muestra_13 = models.FloatField(
        verbose_name='muestra_13',
        blank=True,
        null=True,
    )
    cumple = models.CharField(
        max_length=40,
        verbose_name='Cumple',
        default='Cumple'
    )

    especificacion_list = [
        'Largo',
        'Ancho',
        'Fuelle',
        'Peso',
    ]

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Inspeccion a dimensiones mp'
        verbose_name_plural = 'Inspecciones a dimensiones mp'
        db_table = 'Inspecciones a dimensiones mp'
        ordering = ['-id']
