# Generated by Django 3.2.6 on 2023-02-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_produccion', '0013_alter_controlproduccion_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiemposparadascontrolproduccion',
            name='observacion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observación'),
        ),
    ]
