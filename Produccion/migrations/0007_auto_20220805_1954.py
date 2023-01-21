# Generated by Django 3.2.6 on 2022-08-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0006_auto_20220805_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccion',
            name='aprobacion',
        ),
        migrations.AddField(
            model_name='produccion',
            name='aprobacion_material',
            field=models.BooleanField(default=False, verbose_name='Aprobación material'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='aprobacion_orden',
            field=models.BooleanField(default=False, verbose_name='Aprobación orden'),
        ),
    ]
