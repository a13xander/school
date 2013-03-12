from django.conf.urls import patterns, url
from CodeSchool import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
    url(r'^$','WebSchool.views.login_school'),
    url(r'^logout_school/$','WebSchool.views.logout_school'),
    url(r'^welcome_administrator/$','WebSchool.views.welcome_administrator'),
    url(r'^base_administrator/$','WebSchool.views.base_administrator'),
    url(r'^courses/$','WebSchool.views.courses'),
    url(r'^courses/new_course/$','WebSchool.views.add_course'),
    url(r'^courses/edit_course/(?P<id_course>\d+)$','WebSchool.views.edit_course'),
    url(r'^courses/delete_course/(?P<id_course>\d+)$','WebSchool.views.delete_course'),
    url(r'^goals/$','WebSchool.views.goals'),
    url(r'^goals/new_goal/$','WebSchool.views.add_goal'),
    url(r'^goals/edit_goal/(?P<id_goal>\d+)$','WebSchool.views.edit_goal'),
    url(r'^goals/delete_goal/(?P<id_goal>\d+)$','WebSchool.views.delete_goal'),
    url(r'^grades/$','WebSchool.views.grades'),
    url(r'^grades/new_grade/$','WebSchool.views.add_grade'),
    url(r'^grades/edit_grade/(?P<id_grade>\d+)$','WebSchool.views.edit_grade'),
    url(r'^grades/delete_grade/(?P<id_grade>\d+)$','WebSchool.views.delete_grade'),
    url(r'^headquarters/$','WebSchool.views.headquarters'),
    url(r'^headquarters/new_headquarter/$','WebSchool.views.add_headquarter'),
    url(r'^headquarters/edit_headquarter/(?P<id_headquarter>\d+)$','WebSchool.views.edit_headquarter'),
    url(r'^headquarters/delete_headquarter/(?P<id_headquarter>\d+)$','WebSchool.views.delete_headquarter'),
    url(r'^qualifications/$','WebSchool.views.qualifications'),
    url(r'^qualifications/new_qualification/$','WebSchool.views.add_qualification'),
    url(r'^qualifications/edit_qualification/(?P<id_qualification>\d+)$','WebSchool.views.edit_qualification'),
    url(r'^qualifications/delete_qualification/(?P<id_qualification>\d+)$','WebSchool.views.delete_qualification'),
    url(r'^reports/$','WebSchool.views.reports'),
    url(r'^reports/new_report/$','WebSchool.views.add_report'),
    url(r'^reports/edit_report/(?P<id_report>\d+)$','WebSchool.views.edit_report'),
    url(r'^reports/delete_report/(?P<id_report>\d+)$','WebSchool.views.delete_report'),
    url(r'^students/$','WebSchool.views.students'),
    url(r'^students/new_student/$','WebSchool.views.add_student'),
    url(r'^students/edit_student/(?P<id_student>\d+)$','WebSchool.views.edit_student'),
    url(r'^students/delete_student/(?P<id_student>\d+)$','WebSchool.views.delete_student'),
    url(r'^subjects/$','WebSchool.views.subjects'),
    url(r'^subjects/new_subject/$','WebSchool.views.add_subject'),
    url(r'^subjects/edit_subject/(?P<id_subject>\d+)$','WebSchool.views.edit_subject'),
    url(r'^subjects/delete_subject/(?P<id_subject>\d+)$','WebSchool.views.delete_subject'),
    url(r'^teachers/$','WebSchool.views.teachers'),
    url(r'^teachers/new_teacher/$','WebSchool.views.add_teacher'),
    url(r'^teachers/edit_teacher/(?P<id_teacher>\d+)$','WebSchool.views.edit_teacher'),
    url(r'^teachers/delete_teacher/(?P<id_teacher>\d+)$','WebSchool.views.delete_teacher'),   
)