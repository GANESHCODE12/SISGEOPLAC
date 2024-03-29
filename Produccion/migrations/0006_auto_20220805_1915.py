# Generated by Django 3.2.6 on 2022-08-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0005_remove_produccion_referencia_pigmento'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='aprobacion',
            field=models.BooleanField(default=False, verbose_name='Aprobación'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='cantidad_adicional',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad adicional'),
        ),
    ]
