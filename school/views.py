# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import StudentForm

def new_student(request):
    form = StudentForm()
    return render_to_response('form_new_student.html', {
            'form' : form 
        }, context_instance=RequestContext(request)
    )
