# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-03 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestorObjetos', '0006_auto_20180123_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enunciado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField(help_text='Enunciado identificador para el factor de competencias', verbose_name='Enunciado')),
            ],
            options={
                'verbose_name_plural': 'Enunciados Identificadores',
                'verbose_name': 'Enunciado Identificador',
            },
        ),
        migrations.CreateModel(
            name='Factor_competencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.CharField(help_text='Factor estándar básico de competencias', max_length=80, unique=True, verbose_name='Factor competencias')),
                ('ruta_categoria', models.ForeignKey(help_text='Área fundamental básica', on_delete=django.db.models.deletion.CASCADE, to='gestorObjetos.RutaCategoria', verbose_name='Área básica')),
            ],
            options={
                'verbose_name_plural': 'Factores competencias',
                'verbose_name': 'Factor competencias',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la facultad', max_length=80, unique=True, verbose_name='Facultad')),
            ],
            options={
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominacion', models.CharField(choices=[('gpr', 'Primero'), ('gse', 'Segundo'), ('gte', 'Tercero'), ('gcu', 'Cuarto'), ('gqu', 'Quinto')], default='gpr', help_text='Grado de escolaridad', max_length=3, unique=True, verbose_name='Grado escolar')),
                ('descripcion', models.TextField(blank=True, help_text='Descripción del grado escolar', verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicador', models.TextField(help_text='Indicador para el factor de competencias', verbose_name='indicador')),
                ('enunciado', models.ForeignKey(blank=True, help_text='Enunciado del factor', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Enunciado', verbose_name='Enunciado')),
                ('factor', models.ForeignKey(blank=True, help_text='Factor de Competencias', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Factor_competencias', verbose_name='Factor')),
                ('grados', models.ManyToManyField(help_text='Grado de Escolaridad', to='gestorProyectos.Grado', verbose_name='Grado Escolar')),
            ],
            options={
                'verbose_name_plural': 'Indicadores de Competencia',
                'verbose_name': 'Indicador de Competencia',
            },
        ),
        migrations.CreateModel(
            name='OperacionMental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacion', models.CharField(help_text='Operación mental básica', max_length=80, unique=True, verbose_name='Operación Mental')),
                ('descripcion', models.TextField(help_text='Descripción de la Operación mental básica', verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Operaciones Mentales',
                'verbose_name': 'Operación Mental',
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del parámetro de validación', max_length=80, verbose_name='Parámetro de Validación')),
                ('descripcion', models.TextField(help_text='Descripción del parámetro de validación', verbose_name='Descripción')),
                ('tipo', models.CharField(choices=[('acon', 'Contenido en Relación con los estándares'), ('aenf', 'Enfoque Cognitivo'), ('aeva', 'Evaluación'), ('aint', 'Intercomunicación Estudiante-Material'), ('apos', 'Posibilidades metodológicas')], default='acon', help_text='Tipo parámetro de validación', max_length=4, verbose_name='Asociados a')),
                ('ponderacion', models.DecimalField(decimal_places=2, help_text='Valor porcentual de ponderación del parámetro', max_digits=4, verbose_name='Ponderación Porcentual')),
            ],
            options={
                'verbose_name_plural': 'Parámetros',
                'verbose_name': 'Parámetro',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del programa', max_length=80, unique=True, verbose_name='programa')),
                ('modalidad', models.CharField(choices=[('mpr', 'Presencial'), ('mse', 'Semi presencial'), ('mdi', 'A Distancia'), ('mvi', 'Virtual')], default='mpr', help_text='Modalidad del programa', max_length=3, verbose_name='Modalidad')),
                ('sede', models.CharField(choices=[('ssa', 'San Gil'), ('sch', 'Chiquinquirá'), ('syo', 'Yopal'), ('sse', 'Seres')], default='ssa', help_text='Sede del programa', max_length=3, verbose_name='Sede')),
                ('facultad', models.ForeignKey(help_text='Nombre de la facultad', on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Facultad', verbose_name='Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('fecha', models.DateTimeField(help_text='Fecha en que el Proyecto es aprobado', verbose_name='Fecha de aprobación')),
                ('fase', models.CharField(choices=[('f1', 'Fase 1'), ('f2', 'Fase 2'), ('f3', 'Fase 3')], default='f1', help_text='Movimiento de fase automático', max_length=2)),
                ('calificacion', models.CharField(choices=[('s', 'Sin calificar'), ('a', 'Clasificado'), ('r', 'No Clasificado')], default='s', help_text='Calificación final del proyecto', max_length=1)),
                ('nota', models.DecimalField(decimal_places=2, help_text='Nota numérica de la validación del proyecto', max_digits=4, verbose_name='Nota Porcentual')),
                ('indicadores', models.ManyToManyField(blank=True, help_text='Relacione el/los Indicador (es) de comptencia', null=True, to='gestorProyectos.Indicador', verbose_name='Indicador de Competencia')),
                ('operaciones', models.ManyToManyField(blank=True, help_text='Relacione la/las Operación (es) Mental (es) básica (s) para el proyecto', null=True, to='gestorProyectos.OperacionMental', verbose_name='Operaciones Mentales')),
            ],
        ),
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('valoracion', models.CharField(choices=[('0.0', 'Sin Calificar'), ('10.0', 'Totalmente'), ('7.0', 'Medianamente'), ('5.0', 'Escasamente'), ('2.5', 'No Cumple')], default='0.0', max_length=4, verbose_name='Valoración')),
                ('observaciones', models.TextField(blank=True, help_text='Opcional', verbose_name='Observaciones')),
                ('parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Parametro')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Proyecto')),
            ],
            options={
                'verbose_name_plural': 'Validaciones',
                'verbose_name': 'Validación',
            },
        ),
        migrations.AddField(
            model_name='proyecto',
            name='parametros',
            field=models.ManyToManyField(blank=True, null=True, through='gestorProyectos.Validacion', to='gestorProyectos.Parametro'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='programa',
            field=models.ForeignKey(help_text='Programa académico al que pertenece el proyecto', on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Programa', verbose_name='Programa'),
        ),
        migrations.AddField(
            model_name='enunciado',
            name='factor',
            field=models.ForeignKey(help_text='Factor de Competencias', on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Factor_competencias', verbose_name='Factor'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='indicador',
            order_with_respect_to='factor',
        ),
        migrations.AlterOrderWithRespectTo(
            name='enunciado',
            order_with_respect_to='factor',
        ),
    ]