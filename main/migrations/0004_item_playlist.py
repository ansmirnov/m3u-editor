# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-14 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161014_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='playlist',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Playlist'),
        ),
    ]
