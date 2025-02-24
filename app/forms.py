from django import forms
from django.contrib.auth.models import User
from .models import Student,Teacher,Attendance
class Student_Registration(forms.ModelForm):
    class Meta:
        model= Student
        fields = ['username', 'password']

class Teacher_Registration(forms.ModelForm):
    class Meta : 
        model = Teacher
        fields = ['username', 'password']

class AttendanceForm(forms.ModelForm):
    class Meta :
        model = Attendance
        fields = ['student','subject','date','is_present']