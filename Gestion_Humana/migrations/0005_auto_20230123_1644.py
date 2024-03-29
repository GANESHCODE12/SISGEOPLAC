# Generated by Django 3.2.6 on 2023-01-23 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Humana', '0004_auto_20221026_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesosdisciplinarios',
            name='acta',
            field=models.FileField(blank=True, null=True, upload_to='Gestion_Humana/Actas_descargos', verbose_name='Acta de descargos'),
        ),
        migrations.AlterField(
            model_name='procesosdisciplinarios',
            name='carta_citacion',
            field=models.FileField(blank=True, null=True, upload_to='Gestion_Humana/Cartas_citacion', verbose_name='Carta de citación a descargos'),
        ),
        migrations.AlterField(
            model_name='procesosdisciplinarios',
            name='decision',
            field=models.CharField(choices=[('Por definir', 'Por definir'), ('Llamada de atención', 'Llamada de atención'), ('Sanción', 'Sanción'), ('Despido', 'Despido')], max_length=30, verbose_name='Decisión'),
        ),
        migrations.CreateModel(
            name='ExamenesMedicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_examen', models.DateField(verbose_name='Fecha de examen')),
                ('motivo', models.CharField(choices=[('Periodico', 'Periodico'), ('Egreso', 'Egreso'), ('Ingreso', 'Ingreso')], max_length=50, verbose_name='Cargo')),
                ('resultados', models.FileField(blank=True, null=True, upload_to='Gestion_Humana/Resultados', verbose_name='Resultados')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Humana.informacioncolaborador', verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Examen Medico',
                'verbose_name_plural': 'Examenes medicos',
                'db_table': 'Examenes medicos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EntregaDotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateField(blank=True, null=True, verbose_name='Fecha de entrega')),
                ('documento_entrega', models.FileField(blank=True, null=True, upload_to='Gestion_Humana/entrega_dotacion', verbose_name='Documento de entrega')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Humana.informacioncolaborador', verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Entrega Dotacion',
                'verbose_name_plural': 'Entrega dotaciones',
                'db_table': 'entrega dotacion',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tema de la capacitación')),
                ('fecha_capacitacion', models.DateField(blank=True, null=True, verbose_name='Fecha de la capacitación')),
                ('certificado_capacitacion', models.FileField(blank=True, null=True, upload_to='Gestion_Humana/Certificado_capacitacion', verbose_name='Certificado de capacitación')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Humana.informacioncolaborador', verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Capacitacion',
                'verbose_name_plural': 'Capacitaciones',
                'db_table': 'Capacitaciones',
                'ordering': ['-id'],
            },
        ),
    ]
