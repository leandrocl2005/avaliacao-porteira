# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171120_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='projeto',
        ),
        migrations.AddField(
            model_name='projeto',
            name='aluno',
            field=models.ManyToManyField(to='core.Aluno'),
        ),
        migrations.RemoveField(
            model_name='avaliador',
            name='projeto',
        ),
        migrations.AddField(
            model_name='avaliador',
            name='projeto',
            field=models.ManyToManyField(to='core.Projeto'),
        ),
    ]
