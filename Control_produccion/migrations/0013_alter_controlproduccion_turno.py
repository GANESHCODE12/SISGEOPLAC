# Generated by Django 3.2.6 on 2023-01-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_produccion', '0012_rename_segundos_tiemposparadascontrolproduccion_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlproduccion',
            name='turno',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=30, verbose_name='Turno'),
        ),
    ]
