# Generated by Django 3.2.6 on 2022-10-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_calidad', '0013_niveldeinspeccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='niveldeinspeccion',
            name='cantidades_inspeccionar',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidades a inspeccionar'),
        ),
        migrations.AddField(
            model_name='niveldeinspeccion',
            name='letra',
            field=models.CharField(default='', max_length=5),
        ),
    ]
