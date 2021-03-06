# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-20 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dico', '0004_auto_20170105_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='dico.Definition'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='ip_address',
            field=models.GenericIPAddressField(default=''),
            preserve_default=False,
        ),
    ]
