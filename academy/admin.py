from django.contrib import admin

from .models import Course ,Trainer,Student

class CourseAdmin(admin.ModelAdmin):
        list_display=('course_name','description','duration')

class TrainerAdmin(admin.ModelAdmin):
        list_display=('full_name','email','expertise','image')

class StudentAdmin(admin.ModelAdmin):
        list_display=('full_name','email','enrolled_courese','trainer','image')

# Register your models here.
admin.site.register(Course,CourseAdmin)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Student,StudentAdmin)
