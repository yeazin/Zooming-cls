  
from django.shortcuts import redirect, render
from  django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# model import 
from profiles.models import Student, Teacher, User
from classroom.models import ClassRoom

# Register view for teacher
class TeacherRegister(View):
    def get(self,reqeust,*args,**kwargs):

        context ={

        }
        return render(reqeust,'register/signup.html',context)
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mail_check = User.objects.filter(email = username)
        if mail_check:
            messages.warning(request,'Sorry! Email already Exits')
            return redirect('signup')
        elif password1 != password2:
            messages.warning(request,'Sorry Password Didnot Match')
            return redirect('signup')
        elif len(password1) < 5:
            messages.warning(request,'Password Too Short! Atleast 5 character nedeed.')
            return redirect('signup')
        else:
            auth_info ={
                'email':username,
                'password':make_password(password1)
            }
            user = User(**auth_info)
            user.is_teacher = True
            user.save()
        user_obj = Teacher(user=user,name=name)
        user_obj.save()
        messages.success(request, 'Thanks for Singing !!, Login To continue')
        return redirect ('login')


# student register
class StudentRegister(View):
    def get(self,request,*args,**kwargs):

        context ={
        }
        return render(request,'register/signup.html',context)
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        name = request.POST.get('name')
        photo = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mail_check = User.objects.filter(email=username)
        if mail_check:
            messages.warning(request,'Sorry! Email already Exits')
            return redirect('student_register')
        elif password1 != password2:
            messages.warning(request,'Sorry Password Didnot Match')
            return redirect('student_register')
        elif len(password1) < 5:
            messages.warning(request,'Password Too Short! Atleast 5 character nedeed.')
            return redirect('student_register')

        else:
            auth_info ={
                'email':username,
                'password':make_password(password1)
            }
            user = User(**auth_info)
            user.is_student = True
            user.save()
        user_obj = Student(user=user, photo=photo,name = name )
        user_obj.save()
        messages.success(request,'Thanks for Singing !!, Login to Continue')
        return redirect ('login')

# Login View
'''
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register/login.html')
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        passowrd = request.POST.get('password')
        user = authenticate(request,username=username, password=passowrd)
        email_check = User.objects.filter(email=username)
        if user is not None :
            login(request,user)
            check_rule = User.objects.get(email = user )
            if check_rule.is_student :
                return redirect('student')
            else:
                return redirect ('teacher')
        else:
            if not email_check:
                messages.warning(request,'Sorry Your Email Didnot Match')
                return redirect('login')
            else:
                messages.warning(request,'Sorry Your Password Didnot Match')
                return redirect('login')    
'''

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register/login.html')   

    def post(self,request,*args,**kwargs):
        detect = request.POST.get('username')
        passowrd = request.POST.get('password')
        
        match = User.objects.filter(
            Q(username = detect)|
            Q(email = detect)
            # Q(teachers__phone = detect)|
            # Q(students__phone= detect)
        ).first()
        if match:
            email = match.email
            user = authenticate(request,username=email, password=passowrd)
            if user is not None:
                login(request,user)
                return redirect('/')
                if user.is_student:
                    return redirect('student')
                else:
                    return redirect('teacher')
            else:
                messages.warning(request,'Sorry Your Email Didnot Match')
                return redirect('login')
        else:
            messages.warning(request,'Sorry Doesn`t Match')
            return redirect('login')
#Logout View 
class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        logout(request)
        return redirect('/')