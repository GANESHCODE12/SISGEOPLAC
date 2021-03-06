# Generated by Django 3.2.6 on 2022-04-03 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_alter_pruebasensayo_tolerancia_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicasdimensionale',
            name='id_dimensiones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.dimensiones', verbose_name='Dimensión'),
        ),
        migrations.AlterField(
            model_name='caracteristicasdimensionale',
            name='id_producto_c',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='controlatributo',
            name='id_atributo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.atributos', verbose_name='Atributo'),
        ),
        migrations.AlterField(
            model_name='controlatributo',
            name='id_producto_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='normasaplicable',
            name='id_norma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.normas', verbose_name='Norma'),
        ),
        migrations.AlterField(
            model_name='normasaplicable',
            name='id_producto_n',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='pruebasensayo',
            name='id_producto_p',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='pruebasensayo',
            name='id_pruebas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.pruebas', verbose_name='Prueba y/o ensayo'),
        ),
    ]
