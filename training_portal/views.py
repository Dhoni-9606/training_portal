from django.http import HttpResponse
from django.shortcuts import render
from academy.models import Course, Trainer, Student

def home(request):
    context = {
        'course_count': Course.objects.count(),
        'trainer_count': Trainer.objects.count(),
        'student_count': Student.objects.count(),
        'recent_courses': Course.objects.all().order_by('-id')[:3],
    }
    return render(request, 'home.html', context)
