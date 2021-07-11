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

# Class Index
class Index(View):
    def get(self, request,*args,**kwargs):
        '''
        if request.user.is_authenticated:
            mail_check = User.objects.filter(email = request.user.email)
            if mail_check.is_teacher:
                    return redirect('teacher')
            elif mail_check.is_student:
                    return redirect('student')
        '''
        return render(request,'index.html')