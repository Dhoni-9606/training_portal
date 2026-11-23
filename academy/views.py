from django.shortcuts import render
from django.http import HttpResponse
from .models import Course,Trainer,Student
from .forms import StudentForm

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

def student(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'students.html',context)

def enroll(request):
    if request.method == 'POST':
               form = StudentForm(request.POST,request.FILES)
               if form.is_valid():
                   form.save()
               else:
                    print(form.errors)
    form = StudentForm()
    context = {
            'form':form, }
    return render(request, 'enroll.html',context)





 