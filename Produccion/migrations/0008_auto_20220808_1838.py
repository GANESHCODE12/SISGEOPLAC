# Generated by Django 3.2.6 on 2022-08-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0007_auto_20220805_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produccion',
            old_name='cantidad_adicional',
            new_name='pigmento_adicional',
        ),
        migrations.AddField(
            model_name='produccion',
            name='materia_prima_adicional',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Materia prima adicional'),
        ),
    ]
