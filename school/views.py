# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from forms import StudentForm
from models import Student

def new_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return HttpResponseRedirect(reverse('view_student_page', args=[student.pk]))
    return render_to_response('form_new_student.html', {
            'form' : form
        }, context_instance=RequestContext(request)
    )

def show_student(request, student_id):
    student = Student.objects.get(pk = student_id)
    return HttpResponse('Hi!')
