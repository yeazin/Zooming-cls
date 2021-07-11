from django.shortcuts import redirect, render
from  django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# model import 
from profiles.models import Student, Teacher, User
from classroom.models import ClassRoom

# Student dashboard
class StudentDashboard(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,reqeust):
        user = reqeust.user.students
        context = {
                'room':user.s_room.all()
        }
        return render(reqeust,'dashboard/student/student.html',context)  