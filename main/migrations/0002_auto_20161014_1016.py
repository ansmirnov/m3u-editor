# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-14 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='link',
            field=models.CharField(db_index=True, max_length=40),
        ),
    ]
