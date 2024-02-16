# Generated by Django 3.2.6 on 2023-01-17 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0007_auto_20230103_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicasdimensionale',
            name='id_producto_c',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='controlatributo',
            name='id_producto_a',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='normasaplicable',
            name='id_producto_n',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='pruebasensayo',
            name='id_producto_p',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
    ]
