# Generated by Django 3.2.6 on 2022-09-26 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0002_tecnicosoperarios'),
        ('Control_calidad', '0003_cavidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlcalidad',
            name='operario_calidad',
        ),
        migrations.RemoveField(
            model_name='controlcalidad',
            name='tecnico_calidad',
        ),
        migrations.CreateModel(
            name='ColaboradorInspeccionCalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Humana.tecnicosoperarios', verbose_name='Colaborador')),
                ('inspeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Control', to='Control_calidad.controlcalidad')),
            ],
            options={
                'verbose_name': 'Colaborador Inspección Calidad',
                'verbose_name_plural': 'Colaboradores Inpección Calidad',
                'db_table': 'Colaboradores Inpección Calidad',
                'ordering': ['-id'],
            },
        ),
    ]