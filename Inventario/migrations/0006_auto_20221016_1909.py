# Generated by Django 3.2.6 on 2022-10-17 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0013_auto_20220816_2259'),
        ('Inventario', '0005_alter_inventario_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='requisicion_pt',
            name='producto',
        ),
        migrations.AddField(
            model_name='requisicion_pt',
            name='orden',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Produccion.produccion', verbose_name='Producto'),
            preserve_default=False,
        ),
    ]
