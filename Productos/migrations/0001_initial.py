# Generated by Django 3.2.6 on 2022-07-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atributos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas', models.CharField(max_length=255, verbose_name='Caracteristicas')),
                ('especificacion', models.CharField(max_length=255, verbose_name='Especificación')),
                ('observacion', models.CharField(blank=True, max_length=255, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Atributo',
                'verbose_name_plural': 'Atributos',
                'db_table': 'Atributos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CaracteristicasDimensionale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('valor_nominal', models.FloatField(verbose_name='Valor nominal')),
                ('tolerancia_d', models.FloatField(verbose_name='Tolerancia')),
            ],
            options={
                'verbose_name': 'Caracteristica dimensional',
                'verbose_name_plural': 'Caracteristicas dimensionales',
                'db_table': 'Caracteristicas dimensionales',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colores',
                'db_table': 'Colores',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ControlAtributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Control atributo',
                'verbose_name_plural': 'Controles de atributo',
                'db_table': 'Control Atributo',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Dimensiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas_control', models.CharField(max_length=255, verbose_name='Dimensión')),
                ('unidad_medida', models.CharField(max_length=255, verbose_name='Unidad de medida')),
                ('equipo_medicion', models.CharField(max_length=255, verbose_name='Equipo de medición')),
            ],
            options={
                'verbose_name': 'Dimensión',
                'verbose_name_plural': 'Dimensiones',
                'db_table': 'Dimensiones',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255, verbose_name='Código')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'Norma',
                'verbose_name_plural': 'Normas',
                'db_table': 'Normas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NormasAplicable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Normas Aplicables',
                'verbose_name_plural': 'Normas Aplicables',
                'db_table': 'Normas Aplicables',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('Nombre_producto', models.CharField(max_length=255, verbose_name='Nombre del Producto')),
                ('numero_ficha', models.PositiveIntegerField(unique=True, verbose_name='Número de ficha')),
                ('codigo_producto', models.CharField(max_length=255, verbose_name='Código de producto')),
                ('proceso', models.CharField(max_length=50, verbose_name='Proceso')),
                ('version', models.PositiveIntegerField(verbose_name='Versión')),
                ('fecha_vigencia', models.DateField(verbose_name='Fecha de vigencia')),
                ('tipo_producto', models.CharField(max_length=20, verbose_name='Tipo de producto')),
                ('cliente_especifico', models.CharField(max_length=40, verbose_name='Cliente')),
                ('estado_ficha', models.CharField(choices=[('Vigente', 'Vigente'), ('Obsoleto', 'Obsoleto'), ('En aprobación', 'En aprobación'), ('En revisión', 'En revisión')], default='Vigente', max_length=40, verbose_name='Estado de ficha')),
                ('cavidades', models.PositiveIntegerField(verbose_name='Cavidades')),
                ('peso', models.FloatField(verbose_name='Peso')),
                ('material', models.CharField(max_length=255, verbose_name='Material')),
                ('ciclo', models.PositiveIntegerField(verbose_name='Ciclo')),
                ('descripción_especificaciones', models.CharField(max_length=255, verbose_name='Descripción de especificaciones')),
                ('olor', models.CharField(max_length=255, verbose_name='Olor')),
                ('sabor', models.CharField(max_length=255, verbose_name='Sabor')),
                ('pigmento', models.CharField(max_length=255, verbose_name='Pigmento')),
                ('tipo', models.CharField(max_length=255, verbose_name='Tipo')),
                ('unidad_empaque', models.PositiveIntegerField(verbose_name='Unidad de empaque')),
                ('forma_empaque', models.CharField(max_length=255, verbose_name='Forma de empaque')),
                ('caja', models.CharField(max_length=255, verbose_name='Tamaño de caja')),
                ('bolsa', models.CharField(max_length=255, verbose_name='Tipo de bolsa')),
                ('plano', models.CharField(max_length=255, verbose_name='Código del plano')),
                ('fecha_plano', models.DateField(verbose_name='Fecha del plano')),
                ('diagrama', models.ImageField(blank=True, null=True, upload_to='Produccion/plane', verbose_name='Diagrama')),
                ('vida_util', models.TextField(blank=True, verbose_name='Vida útil')),
                ('elaborado', models.CharField(max_length=255, verbose_name='Elaborado por')),
                ('revisado', models.CharField(max_length=255, verbose_name='Revisado por')),
                ('aprobado', models.CharField(max_length=255, verbose_name='Aprobado por')),
                ('notas', models.TextField(blank=True, verbose_name='Notas')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Productos_colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variables', models.CharField(max_length=255, verbose_name='Variables')),
                ('descripcion_prueba', models.CharField(max_length=255, verbose_name='Descripción de la prueba')),
                ('medio_control', models.CharField(max_length=255, verbose_name='Medio de control')),
            ],
            options={
                'verbose_name': 'Prueba',
                'verbose_name_plural': 'Pruebas',
                'db_table': 'Pruebas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PruebasEnsayo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('tolerancia_p', models.FloatField(verbose_name='Tolerancia')),
            ],
            options={
                'verbose_name': 'Prueba y/o Ensayo',
                'verbose_name_plural': 'Pruebas y/o Ensayos',
                'db_table': 'Prueba_Ensayo',
                'ordering': ['-id'],
            },
        ),
    ]
