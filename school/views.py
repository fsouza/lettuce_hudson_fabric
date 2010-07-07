# Create your views here.
from django.http import HttpResponse

def new_student(request):
    return HttpResponse('Hi!')
