# Generated by Django 3.2.6 on 2022-07-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('numero_op', models.BigAutoField(primary_key=True, serialize=False, unique=True, verbose_name='Número de orden')),
                ('lote', models.CharField(blank=True, max_length=30, verbose_name='Lote')),
                ('orden_compra', models.CharField(max_length=40, verbose_name='Orden de compra')),
                ('cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('cantidad_requerida', models.PositiveIntegerField(verbose_name='Cantidad requerida')),
                ('maquina', models.CharField(blank=True, max_length=40, verbose_name='Máquina')),
                ('estado_op', models.CharField(choices=[('En espera', 'En espera'), ('Detenida', 'Detenida'), ('En producción', 'En producción'), ('Terminada', 'Terminada'), ('Rechazada', 'Rechazada'), ('En proceso', 'En reproceso')], default='En espera', max_length=30, verbose_name='Estado de la orden')),
                ('referencia_pigmento', models.CharField(blank=True, max_length=20, verbose_name='Referencia pigmento')),
                ('fecha_entrega', models.DateField(verbose_name='Fecha de entrega')),
                ('observaciones', models.TextField(blank=True, max_length=800, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Produccion',
                'verbose_name_plural': 'Ordenes de produccion',
                'db_table': 'Ordenes de producción',
                'ordering': ['-numero_op'],
            },
        ),
    ]
