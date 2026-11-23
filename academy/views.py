from django.shortcuts import render
from django.http import HttpResponse
from .models import Course,Trainer

# Create your views here.

def course(request):
    courses=Course.objects.all()
    print(courses)
    context ={
        'courses': courses
    }
    return render(request,'courses.html',context)

def trainer(request):
    trainers=Trainer.objects.all()
    context={
        'trainers':trainers
    }
    return render(request,'trainers.html',context)

 