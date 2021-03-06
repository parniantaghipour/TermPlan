from django.urls import re_path, path

from src.views import courses_list, add_course, delete_course, schedule, graduation, add_passed_course, show_remained, \
    SemesterCourseAddView, ChartTableAddView, ChartCourseAddView, homepage, log_in, sign_up, log_out

app_name = 'src'
urlpatterns = [
    re_path(r'^courses_list/?$', courses_list),
    re_path(r'^add_course/?$', add_course),
    re_path(r'^delete_course/?$', delete_course),
    re_path(r'^schedule/?$', schedule),
    re_path(r'^graduation/?$', graduation),
    re_path(r'^add_passed_course/?$', add_passed_course),
    re_path(r'^remained_courses/?$', show_remained),
    re_path(r'^upload_semester_file/?$', SemesterCourseAddView.as_view(), name='sem_upload_file'),
    re_path(r'^upload_tables_file/?$', ChartTableAddView.as_view(), name='table_upload_file'),
    re_path(r'^upload_courses_file/?$', ChartCourseAddView.as_view(), name='course_upload_file'),
    re_path('^login/?$', log_in),
    re_path('^signup/?$', sign_up),
    re_path('^logout/?$', log_out),
    path('', homepage, name='home'),

]
