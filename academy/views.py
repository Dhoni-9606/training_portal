from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def course(request):
    courses=Course.objects.all()

    print(courses)
    return HttpResponse("this all are the courses")
 