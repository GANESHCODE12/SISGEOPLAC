# Generated by Django 3.2.6 on 2023-01-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_prima_insumo',
            name='categoria',
            field=models.CharField(choices=[('Materia Prima', 'Materia Prima'), ('Insumo', 'Insumo'), ('Pigmento', 'Pigmento')], max_length=30, verbose_name='Categoria'),
        ),
    ]
