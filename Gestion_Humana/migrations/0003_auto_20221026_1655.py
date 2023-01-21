# Generated by Django 3.2.6 on 2022-10-26 21:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0002_tecnicosoperarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacioncolaborador',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='informacioncolaborador',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]