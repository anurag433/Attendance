from django.contrib import admin
from .models import Student,Teacher,Subject,Attendance
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)