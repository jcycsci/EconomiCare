# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20160811_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='new_distance',
            field=models.FloatField(default=3),
        ),
    ]
