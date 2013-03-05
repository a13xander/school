from django.conf.urls import patterns, url
from CodeSchool import settings

urlpatterns = patterns('',
    url(r'^$','WebSchool.views.login_school'),
    url(r'^welcome_administrator/$','WebSchool.views.welcome_administrator'),
    url(r'^logout_school/$','WebSchool.views.logout_school'),
    url(r'^base_administrator/$','WebSchool.views.base_administrator'),
    url(r'^qualifications/$','WebSchool.views.qualifications'),
    url(r'^subjects/$','WebSchool.views.subjects'),
    url(r'^teachers/$','WebSchool.views.teachers'),
    url(r'^reports/$','WebSchool.views.reports'),
    url(r'^goals/$','WebSchool.views.goals'),
    url(r'^grades/$','WebSchool.views.grades'),
    url(r'^courses/$','WebSchool.views.courses'),
    url(r'^students/$','WebSchool.views.students'),
    url(r'^headquarters/$','WebSchool.views.headquarters'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)