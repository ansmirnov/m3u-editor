__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.conf.urls import url
from main import views

urlpatterns = [

    url(r'playlist/([-0-9a-zA-Z]*)', views.fetch_playlist),
]
