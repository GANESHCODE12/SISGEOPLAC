# Generated by Django 3.2.6 on 2022-07-30 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_remove_producto_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos_colores',
            options={'ordering': ['-id'], 'verbose_name': 'Producto Color', 'verbose_name_plural': 'Productos por color'},
        ),
        migrations.AlterModelTable(
            name='productos_colores',
            table='Productos Color',
        ),
        migrations.AlterModelTable(
            name='pruebasensayo',
            table='Pruebas Ensayos',
        ),
    ]