# Generated by Django 3.2.6 on 2023-01-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0015_desarrollo_fecha_analisis_muestras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desarrollo',
            name='fecha_fabricacion',
            field=models.DateField(null=True, verbose_name='Fecha fabricación de las muestras'),
        ),
    ]
