from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    password = models.CharField(max_length=15)

class Teacher(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    password = models.CharField(max_length=15)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ManyToManyField(Student,related_name='subject')


class Attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='Subject_attendances')
    date = models.DateField()
    is_present = models.BooleanField(default=False)