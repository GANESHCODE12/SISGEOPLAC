# Generated by Django 3.2.6 on 2023-01-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0005_auto_20230123_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacioncolaborador',
            name='activo',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=20),
        ),
    ]