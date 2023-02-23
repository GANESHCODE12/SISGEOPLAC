"""Modelo Gestión Humana"""

# Django
from django.db import models
from django.forms import model_to_dict

# Plasmotec
from Plasmotec.settings import MEDIA_URL, STATIC_URL

# Utilidades
from crum import get_current_user
from datetime import date


# Modelo de información General
class InformacionColaborador(models.Model):

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    nombres = models.CharField(
        max_length=50,
        verbose_name="Nombres"
    )
    apellidos = models.CharField(
        max_length=50,
        verbose_name="Apellidos"
    )
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha de nacimiento',
    )
    tipos_documentos_list = [
        ('Cedula', 'Cedula'),
        ('Cedula de extrangeria', 'Cedula de extrangeria'),
    ]
    tipo_documento = models.CharField(
        max_length=40,
        choices=tipos_documentos_list,
        verbose_name="Tipo de documento",
    )
    numero_documento = models.PositiveIntegerField(
        verbose_name="Número de documento",
    )
    fotocopia_documento = models.FileField(
        upload_to='Gestion_Humana/Documento',
        verbose_name='Fotocopia documento',
        null=True,
        blank=True,
    )
    hijos = models.PositiveIntegerField(
        verbose_name="Hijos",
        null=True,
        blank=True,
    )
    hoja_vida = models.FileField(
        upload_to='Gestion_Humana/Curriculum',
        verbose_name='Hoja de vida',
        null=True,
        blank=True,
    )
    certificado_laboral = models.FileField(
        upload_to='Gestion_Humana/Certificados_laborales',
        verbose_name='Certificaciones laborales',
        null=True,
        blank=True,
    )
    certificado_academico = models.FileField(
        upload_to='Gestion_Humana/Certificados_academicos',
        verbose_name='Certificaciones académicas',
        null=True,
        blank=True,
    )
    referencias = models.FileField(
        upload_to='Gestion_Humana/Referencias',
        verbose_name='Referencias laborales',
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to='Gestion_Humana/fFotos',
        verbose_name='Foto',
        null=True,
        blank=True,
    )
    telefono_contacto = models.PositiveIntegerField(
        verbose_name="Teléfono de contacto",
    )
    nombre_emergencia = models.CharField(
        max_length=150,
        verbose_name="Nombres y apellidos contacto de emergencia",
    )
    parentezco = models.CharField(
        max_length=60,
        verbose_name="Parentezco",
    )
    telefono_emergencia = models.PositiveIntegerField(
        verbose_name="Teléfono de contacto de emergencia",
    )
    jefe_inmediato = models.CharField(
        max_length=60,
        verbose_name="Jefe inmediato",
    )
    tipo_contrato_list = [
        ('Indefinido', 'Indefinido'),
        ('Fijo', 'Fijo'),
        ('Obra o labor', 'Obra o labor'),
        ('Aprendizaje', 'Aprendizaje'),
        ('Temporal', 'Temporal'),
        ('Ocasional', 'Ocasional'),
        ('Accidental', 'Accidental')
    ]
    tipo_contrato = models.CharField(
        max_length=50,
        choices=tipo_contrato_list,
        verbose_name="Tipo de contrato",
    )
    contrato = models.FileField(
        upload_to='Gestion_Humana/Contratos',
        verbose_name='Contrato',
        null=True,
        blank=True,
    )
    afiliaciones = models.FileField(
        upload_to='Gestion_Humana/Afiliaciones',
        verbose_name='Afiliaciones',
        null=True,
        blank=True,
    )
    examen_ingreso = models.FileField(
        upload_to='Gestion_Humana/Examenes',
        verbose_name='Examenes de ingreso',
        null=True,
        blank=True,
    )
    carta_terminacion = models.FileField(
        upload_to='Gestion_Humana/Terminacion',
        verbose_name='Carta terminación de contrato',
        null=True,
        blank=True,
    )
    cargo = models.CharField(
        max_length=60,
        verbose_name="Cargo",
    )
    proceso = models.CharField(
        max_length=60,
        verbose_name="Proceso al que pertenece",
    )
    fecha_vinculacion = models.DateField(
        verbose_name='Fecha de vinculación',
    )
    fecha_desvinculacion = models.DateField(
        verbose_name='Fecha de desvinculación',
        null=True,
        blank=True,
    )
    lista_activo = [
        ('Activo','Activo'),
        ('Inactivo', 'Inactivo')
    ]
    activo = models.CharField(
        max_length=20,
        choices=lista_activo,
        default='Activo'
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        db_table = 'Colaboradores'
        ordering = ['-id']

    def __str__(self):
        return '{} {}'.format(
            self.nombres, self.apellidos
        )

    def get_foto(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')

    def get_edad(self):
        return date.today().year - self.fecha_nacimiento.year

    def get_antiguedad(self):
        if self.fecha_desvinculacion:
            fecha = (self.fecha_desvinculacion - self.fecha_vinculacion).days
            return '{:.0f} Meses'.format(fecha / 30.417)
        elif (date.today() - self.fecha_vinculacion).days > 1:
            meses = (date.today() - self.fecha_vinculacion).days
            return '{:.0f} Meses'.format(meses / 30.417)

    def get_hoja_vida(self):
        if self.hoja_vida:
            return '{}{}'.format(MEDIA_URL, self.hoja_vida)

    def get_certificado_laboral(self):
        if self.certificado_laboral:
            return '{}{}'.format(MEDIA_URL, self.certificado_laboral)

    def get_certificado_academico(self):
        if self.certificado_academico:
            return '{}{}'.format(MEDIA_URL, self.certificado_academico)

    def get_referencias(self):
        if self.referencias:
            return '{}{}'.format(MEDIA_URL, self.referencias)

    def get_contrato(self):
        if self.contrato:
            return '{}{}'.format(MEDIA_URL, self.contrato)

    def get_afiliaciones(self):
        if self.afiliaciones:
            return '{}{}'.format(MEDIA_URL, self.afiliaciones)

    def get_examen_ingreso(self):
        if self.examen_ingreso:
            return '{}{}'.format(MEDIA_URL, self.examen_ingreso)

    def get_fotocopia_documento(self):
        if self.fotocopia_documento:
            return '{}{}'.format(MEDIA_URL, self.fotocopia_documento)

    def get_carta_terminacion(self):
        if self.carta_terminacion:
            return '{}{}'.format(MEDIA_URL, self.carta_terminacion)

    def toJSON(self):
        item = model_to_dict(
            self,
            exclude=[
                'hoja_vida',
                'certificado_laboral',
                'certificado_academico',
                'referencias',
                'contrato',
                'afiliaciones',
                'examen_ingreso',
                'fotocopia_documento',
                'carta_terminacion'
            ]
        )
        item['foto'] = self.get_foto()
        item['edad'] = self.get_edad()
        item['antiguedad'] = self.get_antiguedad()
        return item


# Modelo para los otro si
class OtroSi(models.Model):

    colaborador = models.ForeignKey(
        InformacionColaborador,
        on_delete=models.CASCADE,
        verbose_name="Colaborador"
    )

    tema = models.CharField(
        max_length=40,
        verbose_name="Tema del otro si"
    )

    otro_si = models.FileField(
        upload_to='Gestion_Humana/Otro_Si',
        verbose_name='Otro si',
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Otro Si'
        verbose_name_plural = 'Otro Si'
        db_table = 'Otro Si'
        ordering = ['-id']

    def __str__(self):
        return 'Otro si No.{}, tema: {}, del colaborador {} {}'.format(
            self.id, self.tema, self.colaborador.nombres, self.colaborador.apellidos
        )

    def get_otro_si(self):
        return '{}{}'.format(MEDIA_URL, self.otro_si)

    def toJSON(self):
        item = model_to_dict(
            self,
            exclude=[
                'otro_si'
            ]
        )
        item['otro_si'] = self.get_otro_si()
        return item


# Modelo de procesos disciplinarios
class ProcesosDisciplinarios(models.Model):

    colaborador = models.ForeignKey(
        InformacionColaborador,
        on_delete=models.CASCADE,
        verbose_name="Colaborador"
    )

    informe_falta = models.TextField(
        verbose_name="Informe de la falta"
    )

    carta_citacion = models.FileField(
        upload_to='Gestion_Humana/Cartas_citacion',
        verbose_name='Carta de citación a descargos',
        null=True,
        blank=True
    )

    acta = models.FileField(
        upload_to='Gestion_Humana/Actas_descargos',
        verbose_name='Acta de descargos',
        null=True,
        blank=True
    )

    decision_list = [
        ('Por definir', 'Por definir'),
        ('Llamada de atención', 'Llamada de atención'),
        ('Sanción', 'Sanción'),
        ('Despido', 'Despido')
    ]

    decision = models.CharField(
        max_length=30,
        choices=decision_list,
        verbose_name="Decisión"
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Proceso disciplinario'
        verbose_name_plural = 'Procesos disciplinarios'
        db_table = 'Procesos disciplinarios'
        ordering = ['-id']

    def __str__(self):
        return 'Proceso No.{}, del colaborador {} {}'.format(
            self.id, self.colaborador.nombres, self.colaborador.apellidos
        )

    def get_carta_citacion(self):
        return '{}{}'.format(MEDIA_URL, self.carta_citacion)

    def get_acta(self):
        return '{}{}'.format(MEDIA_URL, self.acta)

    def toJSON(
        self,
        exclude=[
            'carta_citacion'
        ]
    ):
        item = model_to_dict(self)
        item['carta_citacion'] = self.get_carta_citacion()
        item['acta'] = self.get_acta()
        return item


# Modelo de técnicos y operarios
class TecnicosOperarios(models.Model):

    nombre = models.CharField(
        max_length=80,
        verbose_name="Nombre Completo"
    )

    cargo_list = [
        ('Técnico', 'Técnico'),
        ('Operario', 'Operario'),
        ('Analista', 'Analista'),
        ('Operario lider', 'Operario lider'),
        ('MYM', 'MYM'),
        ('Jefe producción', 'Jefe producción'),
        ('Jefe calidad', 'Jefe calidad'),
        ('Jefe operativo', 'Jefe operativo'),
    ]

    cargo = models.CharField(
        max_length=50,
        choices=cargo_list,
        verbose_name="Cargo"
    )

    codigo = models.CharField(
        max_length=50,
        verbose_name="Código"
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Técnicos y Operarios'
        verbose_name_plural = 'Técnicos y Operarios'
        db_table = 'Técnicos y Operarios'
        ordering = ['-id']

    def __str__(self):
        return '{} {} Código: {}'.format(
            self.cargo, self.nombre, self.codigo
        )

    def toJSON(self):
        item = model_to_dict(self)
        return item


# Modelo de entrega dotación
class EntregaDotacion(models.Model):

    colaborador = models.ForeignKey(
        InformacionColaborador,
        on_delete=models.CASCADE,
        verbose_name="Colaborador"
    )

    fecha_entrega = models.DateField(
        verbose_name='Fecha de entrega',
        null=True,
        blank=True
    )

    documento_entrega = models.FileField(
        upload_to='Gestion_Humana/entrega_dotacion',
        verbose_name='Documento de entrega',
        null=True,
        blank=True
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Entrega Dotacion'
        verbose_name_plural = 'Entrega dotaciones'
        db_table = 'entrega dotacion'
        ordering = ['-id']

    def __str__(self):
        return 'Entrega No.{}, del colaborador {} {}'.format(
            self.id, self.colaborador.nombres, self.colaborador.apellidos
        )

    def get_documento_entrega(self):
        return '{}{}'.format(MEDIA_URL, self.documento_entrega)

    def toJSON(
        self,
        exclude=[
            'documento_entrega'
        ]
    ):
        item = model_to_dict(self)
        item['documento_entrega'] = self.get_documento_entrega()
        return item


# Modelo de capacitación
class Capacitacion(models.Model):

    colaborador = models.ForeignKey(
        InformacionColaborador,
        on_delete=models.CASCADE,
        verbose_name="Colaborador"
    )

    tema = models.CharField(
        max_length=50,
        verbose_name="Tema de la capacitación",
        null=True,
        blank=True
    )

    fecha_capacitacion = models.DateField(
        verbose_name='Fecha de la capacitación',
        null=True,
        blank=True
    )

    certificado_capacitacion = models.FileField(
        upload_to='Gestion_Humana/Certificado_capacitacion',
        verbose_name='Certificado de capacitación',
        null=True,
        blank=True
    )


    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitaciones'
        db_table = 'Capacitaciones'
        ordering = ['-id']

    def __str__(self):
        return 'Capacitación {}, del colaborador {} {}'.format(
            self.tema, self.colaborador.nombres, self.colaborador.apellidos
        )

    def get_certificado(self):
        return '{}{}'.format(MEDIA_URL, self.certificado_capacitacion)

    def toJSON(
        self,
        exclude=[
            'certificado_capacitacion'
        ]
    ):
        item = model_to_dict(self)
        item['certificado_capacitacion'] = self.get_certificado()
        return item


# Modelo de examenes médicos
class ExamenesMedicos(models.Model):

    colaborador = models.ForeignKey(
        InformacionColaborador,
        on_delete=models.CASCADE,
        verbose_name="Colaborador"
    )

    fecha_examen = models.DateField(
        verbose_name='Fecha de examen',
    )

    lista_motivo = [
        ('Periodico', 'Periodico'),
        ('Egreso', 'Egreso'),
        ('Ingreso', 'Ingreso')
    ]

    motivo = models.CharField(
        max_length=50,
        choices=lista_motivo,
        verbose_name="Motivo"
    )

    resultados = models.FileField(
        upload_to='Gestion_Humana/Resultados',
        verbose_name='Resultados',
        null=True,
        blank=True
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Examen Medico'
        verbose_name_plural = 'Examenes medicos'
        db_table = 'Examenes medicos'
        ordering = ['-id']

    def __str__(self):
        return 'Examen {}, del colaborador {} {}'.format(
            self.motivo, self.colaborador.nombres, self.colaborador.apellidos
        )

    def get_resultados(self):
        return '{}{}'.format(MEDIA_URL, self.resultados)

    def toJSON(
        self,
        exclude=[
            'resultados'
        ]
    ):
        item = model_to_dict(self)
        item['resultados'] = self.get_resultados()
        return item
