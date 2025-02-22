from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=15,unique=True)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)


class Attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    

