# Generated by Django 3.2.6 on 2022-09-15 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecnicosOperarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre Completo')),
                ('cargo', models.CharField(choices=[('Técnico', 'Técnico'), ('Operario', 'Operario')], max_length=50, verbose_name='Cargo')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Técnicos y Operarios',
                'verbose_name_plural': 'Técnicos y Operarios',
                'db_table': 'Técnicos y Operarios',
                'ordering': ['-id'],
            },
        ),
    ]
