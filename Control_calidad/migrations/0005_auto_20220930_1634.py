# Generated by Django 3.2.6 on 2022-09-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_calidad', '0004_auto_20220926_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pruebascalidad',
            name='metodo_p',
        ),
        migrations.AddField(
            model_name='pruebascalidad',
            name='cavidad_1',
            field=models.FloatField(blank=True, default=0.0, verbose_name='cavidad_1'),
        ),
        migrations.DeleteModel(
            name='Cavidades',
        ),
    ]
