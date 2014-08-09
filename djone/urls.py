from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'djone.views.index', name='index'),
    url(r'^indexph/$', 'djone.views.indexph', name='indexph'),

    url(r'^media(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':True}),

    url(r'^admin/', include(admin.site.urls)),
)
