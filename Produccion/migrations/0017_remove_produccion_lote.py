# Generated by Django 3.2.6 on 2023-01-21 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0016_alter_desarrollo_fecha_fabricacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccion',
            name='lote',
        ),
    ]