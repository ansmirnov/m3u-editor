# -*- coding: utf8 -*-

from django.db import models


class Playlist(models.Model):
    name = models.CharField("Название плейлиста", max_length=100)
    owner = models.ForeignKey('auth.User')
    public = models.BooleanField()
    link = models.CharField(max_length=40, db_index=True)

    def items(self):
        return self.item_set.all()

    def __unicode__(self):
        return self.link


class Item(models.Model):
    name = models.CharField("Название канала", max_length=100)
    source = models.CharField("Адрес потока", max_length=255)
    playlist = models.ForeignKey('Playlist', blank=True, null=True, default=True)
    tvg_name = models.CharField(max_length=100, blank=True)
    tvg_logo = models.CharField(max_length=100, blank=True)
    tvg_id = models.IntegerField(default=0)
    deinterlace = models.IntegerField(default=1)
    time_shift = models.IntegerField(default=0)
    name1 = models.CharField(max_length=100, blank=True)
    mono = models.IntegerField(default=0)
    audiotrack = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.source)


class Group(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    playlist = models.ForeignKey(Playlist)

    def __unicode__(self):
        return self.name
