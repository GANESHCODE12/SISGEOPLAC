# Generated by Django 3.2.6 on 2022-08-04 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0004_alter_produccion_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccion',
            name='referencia_pigmento',
        ),
    ]
