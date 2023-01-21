# Generated by Django 3.2.6 on 2022-07-30 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Produccion', '0002_produccion_producto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Productos', '0001_initial'),
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicion_pt',
            name='requisicion_pt_actualizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requisicion_pt_actualizado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisicion_pt',
            name='requsicion_pt_creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requsicion_pt_creado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisicion',
            name='material_despachado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_despachado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisicion',
            name='material_solicitado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.entrada', verbose_name='Material Solicitado'),
        ),
        migrations.AddField(
            model_name='requisicion',
            name='material_solicitado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_solicitado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisicion',
            name='numero_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produccion.produccion', verbose_name='Orden de Producción'),
        ),
        migrations.AddField(
            model_name='materia_prima_insumo',
            name='material_actualizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_actualizado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='materia_prima_insumo',
            name='material_creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_creado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_actualizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventario_actualizado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_creado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='ingresado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingresado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entrada',
            name='ingreso_actualizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingreso_actualizado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entrada',
            name='ingreso_materia_prima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.materia_prima_insumo', verbose_name='Material Solicitado'),
        ),
    ]
