# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-23 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorObjetos', '0003_auto_20180123_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='grupos',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
