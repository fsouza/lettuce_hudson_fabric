from django.conf.urls.defaults import *

urlpatterns = patterns('school.views',
    url(r'^students/new', 'new_student', name = 'new_students_page'),
)
