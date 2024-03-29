# Generated by Django 3.2.6 on 2023-01-02 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produccion', '0013_auto_20220816_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desarrollo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_desarrollo', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_desarrollo', models.DateTimeField(auto_now=True, null=True)),
                ('producto', models.CharField(max_length=200, verbose_name='Producto')),
                ('ciclo', models.PositiveBigIntegerField(verbose_name='Ciclo')),
                ('solicitado_por', models.CharField(max_length=40, verbose_name='Solicitado por')),
                ('fecha_limite_entrega', models.DateField(verbose_name='Fecha limite de entrega')),
                ('fecha_fabricacion', models.DateField(verbose_name='Fecha fabricación de las muestras')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('tipo_empaque', models.CharField(max_length=60, verbose_name='Tipo de empaque')),
                ('maquina', models.CharField(blank=True, max_length=40, verbose_name='Máquina')),
                ('objetivo_muestra', models.TextField(blank=True, max_length=800, verbose_name='Objetivo  muestra')),
                ('molde_nuevo', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Molde nuevo?')),
                ('es_funcional', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Es funcional?')),
                ('diseño', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Diseño')),
                ('variables', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Variables')),
                ('peso_solicitado', models.PositiveIntegerField(verbose_name='Peso solicitado')),
                ('observaciones', models.TextField(blank=True, max_length=800, verbose_name='Observaciones')),
                ('color', models.CharField(max_length=30, verbose_name='Color')),
                ('dimensional', models.CharField(choices=[('Cumple', 'Cumple'), ('No cumple', 'No cumple'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Cumple con dimensiones?')),
                ('funcional', models.CharField(choices=[('Cumple', 'Cumple'), ('No cumple', 'No cumple'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Cumple con el funcionamiento?')),
                ('atributos', models.CharField(choices=[('Cumple', 'Cumple'), ('No cumple', 'No cumple'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Cumple con atributos?')),
                ('muestras', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Requiere más muestras?')),
                ('autorizacion', models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('No aplica', 'No aplica')], default='No aplica', max_length=30, verbose_name='Requiere autorización?')),
                ('desarrollo_creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollo_creado_por', to=settings.AUTH_USER_MODEL)),
                ('usuario_actualizo_desarrollo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ususario_actualizo_desarrollo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Desarrollo',
                'verbose_name_plural': 'Desarrollos',
                'db_table': 'Desarrollos',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='produccion',
            name='maquina',
            field=models.CharField(choices=[('', ''), ('Inyectora 1', 'Inyectora 1'), ('Inyectora 2', 'Inyectora 2'), ('Inyectora 3', 'Inyectora 3'), ('Inyectora 4', 'Inyectora 4'), ('Inyectora 5', 'Inyectora 5'), ('Inyectora 6', 'Inyectora 6'), ('Sopladora 1', 'Sopladora 1'), ('Sopladora 2', 'Sopladora 2'), ('Sopladora 3', 'Sopladora 3'), ('Maquila', 'Maquila')], default='', max_length=40, verbose_name='Máquina'),
        ),
        migrations.CreateModel(
            name='DesarrolloMuestras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp', models.PositiveBigIntegerField(verbose_name='mp')),
                ('pigmentos', models.PositiveBigIntegerField(verbose_name='pigmentos')),
                ('empaque', models.PositiveBigIntegerField(verbose_name='empaque')),
                ('maquila', models.PositiveBigIntegerField(verbose_name='maquila')),
                ('operario', models.PositiveBigIntegerField(verbose_name='operario')),
                ('tecnico', models.PositiveBigIntegerField(verbose_name='tecnico')),
                ('montaje', models.PositiveBigIntegerField(verbose_name='montaje')),
                ('total', models.PositiveBigIntegerField(verbose_name='total')),
                ('desarrollo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollo_muestras', to='Produccion.desarrollo')),
            ],
            options={
                'verbose_name': 'Desarrollo producción',
                'verbose_name_plural': 'Desarrollos producción',
                'db_table': 'Desarrollos producción',
                'ordering': ['-id'],
            },
        ),
    ]
