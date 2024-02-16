# Generated by Django 3.2.6 on 2023-01-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0006_auto_20220402_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colores',
                'db_table': 'Colores',
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='producto',
            name='codigo_producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='color',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='sabor',
        ),
        migrations.AlterModelTable(
            name='pruebasensayo',
            table='Pruebas Ensayos',
        ),
        migrations.CreateModel(
            name='Productos_colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=255, null=True, verbose_name='Código de producto')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.colores', verbose_name='Color')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Producto Color',
                'verbose_name_plural': 'Productos por color',
                'db_table': 'Productos Color',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='caracteristicasdimensionale',
            name='id_producto_c',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.productos_colores', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='controlatributo',
            name='id_producto_a',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.productos_colores', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='normasaplicable',
            name='id_producto_n',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.productos_colores', verbose_name='Nombre del Producto'),
        ),
        migrations.AlterField(
            model_name='pruebasensayo',
            name='id_producto_p',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Productos.productos_colores', verbose_name='Nombre del Producto'),
        ),
    ]