__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# Examples:
# url(r'^$', 'm3u_editor.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('main.urls')),
]
