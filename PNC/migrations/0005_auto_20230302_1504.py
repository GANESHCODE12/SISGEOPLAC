# Generated by Django 3.2.6 on 2023-03-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNC', '0004_trazabilidadproductonoconforme'),
    ]

    operations = [
        migrations.AddField(
            model_name='productonoconforme',
            name='operario_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 1'),
        ),
        migrations.AddField(
            model_name='productonoconforme',
            name='operario_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 2'),
        ),
        migrations.AddField(
            model_name='productonoconforme',
            name='operario_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 3'),
        ),
        migrations.AddField(
            model_name='productonoconforme',
            name='tecnico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Técnico'),
        ),
        migrations.AddField(
            model_name='trazabilidadproductonoconforme',
            name='operario_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 1'),
        ),
        migrations.AddField(
            model_name='trazabilidadproductonoconforme',
            name='operario_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 2'),
        ),
        migrations.AddField(
            model_name='trazabilidadproductonoconforme',
            name='operario_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Operario 3'),
        ),
        migrations.AddField(
            model_name='trazabilidadproductonoconforme',
            name='tecnico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Técnico'),
        ),
    ]
