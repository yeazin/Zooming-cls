from django.contrib import admin
from .models import User, Teacher, Student

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)