# Generated by Django 3.2.6 on 2022-10-06 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Control_calidad', '0009_auto_20221005_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificadoscalidad',
            name='certificado',
        ),
    ]
