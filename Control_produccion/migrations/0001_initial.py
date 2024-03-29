# Generated by Django 3.2.6 on 2022-07-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('turno', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=30, verbose_name='Turno')),
                ('hora_inicio', models.DateTimeField(verbose_name='Hora inicio')),
                ('hora_final', models.DateTimeField(verbose_name='Hora Final')),
                ('cantidad_producida', models.PositiveIntegerField(verbose_name='Cantidad producida')),
                ('ciclo_turno', models.FloatField(verbose_name='Ciclo turno')),
                ('cavidades_operacion', models.PositiveIntegerField(verbose_name='Cavidades Operación')),
                ('tiempo_paradas', models.DurationField(verbose_name='Tiempo de paradas')),
                ('observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Control orden',
                'verbose_name_plural': 'Controles de produccion',
                'db_table': 'Controles de produccion',
                'ordering': ['-id'],
            },
        ),
    ]
