from django.shortcuts import render
from main.models import *


def fetch_playlist(request, link):
    playlist = Playlist.objects.get(link=link)
    template = 'playlist/m3u.list'
    context = {
        'playlist': playlist,
    }
    return render(request, template, context)
