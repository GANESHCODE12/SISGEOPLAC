# Generated by Django 3.2.6 on 2022-12-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_calidad', '0016_dimensional_cumple'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimensional',
            name='especificacion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Especificación'),
        ),
    ]