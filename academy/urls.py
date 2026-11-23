from django.urls import path
from .import views

urlpatterns=[
    path('course/',views.course,name='course'),
    path('trainer/',views.trainer,name='trainer'),
    path('student/',views.student,name='student'),

]