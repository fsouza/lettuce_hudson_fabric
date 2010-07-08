from django.conf.urls.defaults import *

urlpatterns = patterns('school.views',
    url(r'^students/new$', 'new_student', name = 'new_students_page'),
    url(r'^students/view/(?P<student_id>\d+)$', 'show_student', name = 'view_student_page'),
)
