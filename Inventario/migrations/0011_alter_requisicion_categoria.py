# Generated by Django 3.2.6 on 2023-08-06 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0010_requisicion_control_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicion',
            name='categoria',
            field=models.CharField(default='Insumo', max_length=250, verbose_name='Categoria'),
        ),
    ]