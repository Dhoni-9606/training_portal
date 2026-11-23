from django.db import models

# Create your models here.

class Course(models.Model):
    course_name =models.CharField(max_length=100)
    description =models.CharField(max_length=200)
    duration =models.IntegerField(help_text="durations in weeks")
    # course_image=models.ImageField()
    trainers=models.ManyToManyField('Trainer',related_name="courses",blank=True)

    def __str__(self):
        return self.course_name


class Trainer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    expertise=models.CharField(max_length=100)
    image=models.ImageField(upload_to='trainers/',blank=True,null=True)

    def __str__(self):
        return f"{self.first_name}.{self.last_name}"

    def full_name(self):
            return f"{self.first_name} {self.last_name}"



class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    image=models.ImageField(upload_to='students/',blank=True,null=True)
    is_active=models.BooleanField(default=True)
    enrolled_courese=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True)

    def full_name(self):
                return f"{self.first_name} {self.last_name}"
    



