# Generated by Django 3.2.6 on 2022-09-13 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produccion', '0013_auto_20220816_2259'),
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='verbo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produccion', to='Produccion.produccion'),
        ),
    ]
