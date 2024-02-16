# Generated by Django 3.2.6 on 2023-01-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0001_initial'),
        ('Control_produccion', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivosParadasControlProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Motivo Parada')),
            ],
            options={
                'verbose_name': 'Motivo de parada',
                'verbose_name_plural': 'Motivos de paradas',
                'db_table': 'Motivos de paradas',
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='controlproduccion',
            name='operario',
        ),
        migrations.RemoveField(
            model_name='controlproduccion',
            name='tecnico',
        ),
        migrations.RemoveField(
            model_name='controlproduccion',
            name='tiempo_paradas',
        ),
        migrations.AlterField(
            model_name='controlproduccion',
            name='hora_final',
            field=models.DateTimeField(null=True, verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='controlproduccion',
            name='hora_inicio',
            field=models.DateTimeField(null=True, verbose_name='Hora inicio'),
        ),
        migrations.CreateModel(
            name='TiemposParadasControlProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.PositiveBigIntegerField(null=True, verbose_name='Segundos')),
                ('minutos', models.PositiveBigIntegerField(null=True, verbose_name='Minutos')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Control_Parada', to='Control_produccion.controlproduccion')),
                ('motivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Control_produccion.motivosparadascontrolproduccion', verbose_name='Motivo Parada')),
            ],
            options={
                'verbose_name': 'Tiempo de parada',
                'verbose_name_plural': 'Tiempos de paradas',
                'db_table': 'Tiempos de paradas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ColaboradorControlProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Humana.tecnicosoperarios', verbose_name='Colaborador')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Control', to='Control_produccion.controlproduccion')),
            ],
            options={
                'verbose_name': 'Colaborador Control orden',
                'verbose_name_plural': 'Colaborador Controles de produccion',
                'db_table': 'Colaborador Controles de produccion',
                'ordering': ['-id'],
            },
        ),
    ]