# Generated by Django 3.2.6 on 2023-07-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0008_auto_20230120_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_colores',
            name='dosificacion',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Dosificación'),
        ),
        migrations.AddField(
            model_name='productos_colores',
            name='referencia_pigmento',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Referencia del pigmento'),
        ),
    ]