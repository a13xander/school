from django.conf.urls import patterns, url
from CodeSchool import settings

urlpatterns = patterns('',
    url(r'^$','WebSchool.views.login'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)