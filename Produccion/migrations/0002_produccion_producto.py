# Generated by Django 3.2.6 on 2021-12-10 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '0001_initial'),
        ('Produccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
    ]
