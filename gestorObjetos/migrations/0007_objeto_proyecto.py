# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-10 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProyectos', '0001_initial'),
        ('gestorObjetos', '0006_auto_20180123_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='proyecto',
            field=models.OneToOneField(blank=True, help_text='proyecto tomado como objeto.', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestorProyectos.Proyecto'),
        ),
    ]
