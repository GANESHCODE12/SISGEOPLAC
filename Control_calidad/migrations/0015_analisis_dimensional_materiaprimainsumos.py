# Generated by Django 3.2.6 on 2022-12-26 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventario', '0006_auto_20221016_1909'),
        ('Control_calidad', '0014_auto_20221021_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriaPrimaInsumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('arte_cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Arte cliente')),
                ('unidades_muestra', models.PositiveBigIntegerField(verbose_name='Cantidad de unidades de muestra')),
                ('unidades_lote', models.PositiveBigIntegerField(verbose_name='Cantidad de unidades del lote')),
                ('proveedor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Proveedor')),
                ('fecha_lote', models.DateField(verbose_name='Fecha de fabricación')),
                ('arte_ingreso', models.CharField(blank=True, max_length=100, null=True, verbose_name='Arte ingreso')),
                ('unidades_empaque', models.PositiveBigIntegerField(verbose_name='Cantidad de unidades de empaque revisadas')),
                ('certificado', models.BooleanField(verbose_name='Certificado de calidad')),
                ('especificaciones', models.BooleanField(verbose_name='Cumple especificaciones')),
                ('lote_ingreso', models.BooleanField(verbose_name='Coincide con lote de ingreso')),
                ('observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
                ('revisado_por', models.CharField(blank=True, max_length=100, null=True, verbose_name='Revisado por')),
                ('aprobado', models.BooleanField(verbose_name='Aprobado')),
                ('tolerado', models.BooleanField(verbose_name='Tolerado')),
                ('estado', models.CharField(choices=[('Conforme', 'Conforme'), ('Retenido', 'Retenido'), ('En devolución', 'En devolución'), ('Devuelto', 'Devuelto'), ('Conciliado', 'Conciliado')], default='En espera', max_length=40, verbose_name='Estado del material')),
                ('inspector_calidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspector_calidad_mp', to=settings.AUTH_USER_MODEL)),
                ('inspector_calidad_actualizo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspector_calidad_actualizo_mp', to=settings.AUTH_USER_MODEL)),
                ('materia_prima_insumo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materia_prima_insumo', to='Inventario.entrada')),
            ],
            options={
                'verbose_name': 'Inspección a materia prima e insumos',
                'verbose_name_plural': 'Inspecciones a materia prima e insumos',
                'db_table': 'Inspección materia prima e insumos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Dimensional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muestra_1', models.FloatField(blank=True, null=True, verbose_name='muestra_1')),
                ('muestra_2', models.FloatField(blank=True, null=True, verbose_name='muestra_2')),
                ('muestra_3', models.FloatField(blank=True, null=True, verbose_name='muestra_3')),
                ('muestra_4', models.FloatField(blank=True, null=True, verbose_name='muestra_4')),
                ('muestra_5', models.FloatField(blank=True, null=True, verbose_name='muestra_5')),
                ('muestra_6', models.FloatField(blank=True, null=True, verbose_name='muestra_6')),
                ('muestra_7', models.FloatField(blank=True, null=True, verbose_name='muestra_7')),
                ('muestra_8', models.FloatField(blank=True, null=True, verbose_name='muestra_8')),
                ('muestra_9', models.FloatField(blank=True, null=True, verbose_name='muestra_9')),
                ('muestra_10', models.FloatField(blank=True, null=True, verbose_name='muestra_10')),
                ('muestra_11', models.FloatField(blank=True, null=True, verbose_name='muestra_11')),
                ('muestra_12', models.FloatField(blank=True, null=True, verbose_name='muestra_12')),
                ('muestra_13', models.FloatField(blank=True, null=True, verbose_name='muestra_13')),
                ('inspeccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Analisis_dimensional', to='Control_calidad.materiaprimainsumos')),
            ],
            options={
                'verbose_name': 'Inspeccion a dimensiones mp',
                'verbose_name_plural': 'Inspecciones a dimensiones mp',
                'db_table': 'Inspecciones a dimensiones mp',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Analisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especificacion', models.CharField(max_length=40, verbose_name='Especificación')),
                ('cumple', models.CharField(max_length=40, verbose_name='Cumple')),
                ('inspeccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Analisis', to='Control_calidad.materiaprimainsumos')),
            ],
            options={
                'verbose_name': 'Analisis de atributos y funcional',
                'verbose_name_plural': 'Analisis de atributos y funcional',
                'db_table': 'Analisis de atributos y funcional',
                'ordering': ['-id'],
            },
        ),
    ]
