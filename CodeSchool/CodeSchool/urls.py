from django.conf.urls import patterns, url
from CodeSchool import settings

urlpatterns = patterns('',
    url(r'^$','WebSchool.views.login_school'),
    url(r'^welcome_administrator/$','WebSchool.views.welcome_administrator'),
    url(r'^base_administrator/$','WebSchool.views.base_administrator'),
    url(r'^qualification/$','WebSchool.views.qualification'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)