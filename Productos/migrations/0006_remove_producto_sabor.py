# Generated by Django 3.2.6 on 2022-10-07 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_auto_20221007_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='sabor',
        ),
    ]