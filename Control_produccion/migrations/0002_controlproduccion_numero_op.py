# Generated by Django 3.2.6 on 2021-12-10 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Control_produccion', '0001_initial'),
        ('Produccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlproduccion',
            name='numero_op',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produccion.produccion', verbose_name='Número de orden'),
        ),
    ]