# Generated by Django 3.2.6 on 2021-12-21 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PNC', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productonoconforme',
            name='numero_op',
        ),
    ]
