# Generated by Django 3.2.6 on 2023-08-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_produccion', '0007_auto_20230222_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlproduccion',
            name='material_molido',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad material molido'),
        ),
    ]
