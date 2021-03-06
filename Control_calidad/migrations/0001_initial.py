# Generated by Django 3.2.6 on 2021-12-10 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlCalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('tecnico', models.CharField(max_length=30, verbose_name='Técnico')),
                ('operario', models.CharField(max_length=30, verbose_name='Operario')),
                ('turno', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10, verbose_name='Turno')),
                ('fecha_despacho', models.DateField(null=True, verbose_name='Fecha despacho')),
                ('cantidad_solicitada', models.PositiveIntegerField(default=0, verbose_name='Cantidad solicitada')),
                ('empaque_y_embalaje', models.TextField(blank=True, verbose_name='Empaque y embalaje')),
                ('observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Inspección de calidad',
                'verbose_name_plural': 'Inspecciones de calidad',
                'db_table': 'Inspecciones de calidad',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InspeccionAtributos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_a', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_a', models.DateTimeField(auto_now=True, null=True)),
                ('resultado_ia', models.CharField(choices=[('Conforme', 'Conforme'), ('No conforme', 'No conforme')], max_length=30, verbose_name='Resultado')),
            ],
            options={
                'verbose_name': 'Inspección a atributo',
                'verbose_name_plural': 'Inspecciones a atributos',
                'db_table': 'Inspecciones a atributos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InspeccionDimensional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_d', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_d', models.DateTimeField(auto_now=True, null=True)),
                ('promedio', models.FloatField(verbose_name='Promedio')),
                ('resultado_id', models.CharField(choices=[('Conforme', 'Conforme'), ('No conforme', 'No conforme')], max_length=30, verbose_name='Resultado')),
            ],
            options={
                'verbose_name': 'Inspección a dimensiones',
                'verbose_name_plural': 'Inspecciones a dimensiones',
                'db_table': 'Inspecciones a dimensiones',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_p', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_p', models.DateTimeField(auto_now=True, null=True)),
                ('metodo_p', models.CharField(max_length=40, verbose_name='Método')),
                ('resultado_p', models.CharField(choices=[('Conforme', 'Conforme'), ('No conforme', 'No conforme')], max_length=30, verbose_name='Resultado')),
                ('valor', models.FloatField(verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Inspeccion a prueba',
                'verbose_name_plural': 'Inspecciones a pruebas',
                'db_table': 'Inspecciones a pruebas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_r', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_r', models.DateTimeField(auto_now=True, null=True)),
                ('resultado', models.CharField(choices=[('Conforme', 'Conforme'), ('No conforme', 'No conforme')], max_length=30, verbose_name='Resultado')),
                ('evidencia', models.ImageField(blank=True, null=True, upload_to='Control_calidad/Evidencia', verbose_name='Evidencia')),
                ('id_inspeccion_r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_calidad.controlcalidad', verbose_name='Número de inspección')),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
                'db_table': 'Resultados',
                'ordering': ['-id'],
            },
        ),
    ]
