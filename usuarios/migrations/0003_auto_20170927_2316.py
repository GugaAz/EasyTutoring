# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='curso',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
