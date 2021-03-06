# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-14 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0')),
                ('source', models.CharField(max_length=100, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xbf\xd0\xbe\xd1\x82\xd0\xbe\xd0\xba\xd0\xb0')),
                ('tvg_name', models.CharField(blank=True, max_length=100)),
                ('tvg_logo', models.CharField(blank=True, max_length=100)),
                ('tvg_id', models.IntegerField(default=0)),
                ('deinterlace', models.IntegerField(default=1)),
                ('time_shift', models.IntegerField(default=0)),
                ('name1', models.CharField(blank=True, max_length=100)),
                ('mono', models.IntegerField(default=0)),
                ('audiotrack', models.IntegerField(default=0)),
                ('site_id', models.IntegerField(null=True)),
                ('type_ch', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbb\xd0\xb5\xd0\xb9\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd0\xb0')),
                ('public', models.BooleanField()),
                ('link', models.CharField(max_length=40)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Playlist'),
        ),
    ]
