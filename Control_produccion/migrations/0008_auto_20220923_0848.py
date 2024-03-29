# Generated by Django 3.2.6 on 2022-09-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_produccion', '0007_auto_20220922_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlproduccion',
            name='hora_final',
        ),
        migrations.RemoveField(
            model_name='controlproduccion',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='controlproduccion',
            name='tiempo_total_paradas',
        ),
        migrations.AddField(
            model_name='controlproduccion',
            name='duracion_turno',
            field=models.DurationField(null=True, verbose_name='Duración del turno'),
        ),
        migrations.AddField(
            model_name='controlproduccion',
            name='fecha_tuno',
            field=models.DateField(null=True, verbose_name='Fecha del turno'),
        ),
    ]
