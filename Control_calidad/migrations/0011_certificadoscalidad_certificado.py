# Generated by Django 3.2.6 on 2022-10-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_calidad', '0010_remove_certificadoscalidad_certificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificadoscalidad',
            name='certificado',
            field=models.FileField(null=True, upload_to='Control_calidad/Certificados', verbose_name='Certificado'),
        ),
    ]
