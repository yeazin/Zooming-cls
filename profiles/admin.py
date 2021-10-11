from django.contrib import admin
from .models import User, Teacher, Student

# Register your models here.
admin.site.register(User)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','user','phone']
admin.site.register(Teacher,TeacherAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','user','phone']
admin.site.register(Student,StudentAdmin)