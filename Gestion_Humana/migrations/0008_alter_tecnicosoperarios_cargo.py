# Generated by Django 3.2.6 on 2023-02-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0007_alter_examenesmedicos_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnicosoperarios',
            name='cargo',
            field=models.CharField(choices=[('Técnico', 'Técnico'), ('Operario', 'Operario'), ('Analista', 'Analista'), ('Operario lider', 'Operario lider'), ('MYM', 'MYM'), ('Jefe producción', 'Jefe producción'), ('Jefe calidad', 'Jefe calidad'), ('Jefe operativo', 'Jefe operativo')], max_length=50, verbose_name='Cargo'),
        ),
    ]
