from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom, MemberShip
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# importing custom decorators
from src.decorators import SingleClassForbidden
# Email Configure 
#from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


#create classroom
class CreateClassRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        return render(request,'class/create_class.html')
    
    def post(self,request):
        name = request.POST.get('name')
        unit = request.POST.get('unit')
        detail = request.POST.get('detail')
        user = request.user.teachers
        room = ClassRoom(teacher =user,unit=unit, name=name, details = detail )
        room.save()
        messages.success(request,' Classroom Has Been Created !!')
        return redirect('teacher')

# view All class room
class ViewClassRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,reqeust):
        user = reqeust.user.teachers
        room = user.room.all()
        context = {
            'room':room
        }   
        return render(reqeust,'class/all_class.html',context)

# single class
@method_decorator(SingleClassForbidden,name='dispatch')
class SingleClass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        
        room = get_object_or_404(ClassRoom  ,id=id) 
        stream = room.roomstream_set.all().order_by('-created_at')
        context ={
            'room':room,
            'stream':stream,
            'user':request.user
        } 
        return render(request,'class/single.html', context)

# Join Class
class JoinRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request):
        code = request.POST.get('code')
        try :
            check_code = ClassRoom.objects.get(code = code)
            user = request.user.students
            class_room = ClassRoom(id = check_code.id )
            check = MemberShip.objects.filter(room=class_room, student = user )
            if check :
                messages.success(request,'You are Already a member')
                return redirect('single', id=check_code.id) 
            else:
                member = MemberShip(room= class_room, student = user )
                member.is_join = True 
                member.save()
                messages.success(request,'Welcome to The Class')
                return redirect('single', id=check_code.id )  
        except ClassRoom.DoesNotExist:
            messages.warning(request,'Sorry The Code Didnot Match. Try Again')
            return redirect('student')

# leave Class
class LeaveClass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        user = request.user.students
        room = get_object_or_404(ClassRoom, id=id)
        membership = MemberShip.objects.filter(student=user,room=room)
        membership.delete()
        messages.warning(request,'You have left the Classroom')
        return redirect('student')

class SendMail(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        return render (request,'dashboard/teacher/send_mail.html')

    def post(self,request):
        email = request.POST.get('email')
        code = request.POST.get('code')
        user = request.user
        body = render_to_string('email.html',{
            'code':code,
            'user':user
        })

        if request.POST.get('con'):
            mail = EmailMessage(
                subject ='Join the ClassRoom Now',
                body = body,
                from_email= settings.EMAIL_HOST_USER,
                to = [email]
                )
            mail.content_subtype = "HTML"
            mail.send()
            messages.success(request,'Your Emails has been SENT')
            return redirect('send')
        else:
            mail = EmailMessage(
            subject ='Join the ClassRoom Now',
            body = body,
            from_email= settings.EMAIL_HOST_USER,
            to = [email]
            )
            mail.content_subtype = "HTML"
            mail.send()
            messages.success(request,'Your Email has been SENT')
            return redirect('teacher')

        '''
        send_mail(
            'Join The Class', # Subjects here
            'code', # Body Messages
            settings.EMAIL_HOST_USER, # email sender
            [email], # to reciever email 
            fail_silently=False,
        )
        messages.success(request,'Email has Sent')
        return redirect('teacher')
       
        
        if request.POST.get('continue'):
            email = request.POST.get('email')
            code = request.POST.get('code')
            send_mail(
                'Join The Class', # Subjects here
                'Hi yeasin join the class here and \n code is ' + code + ' get now', # Body Messages
                settings.EMAIL_HOST_USER, # email sender
                [email], # to reciever email 
                fail_silently=False,
            )
            messages.success('Email has Sent')
            return redirect('send')
            
        elif request.POST.get('back'):
            email = request.POST.get('email')
            code = request.POST.get('code')
            send_mail(
                'Join The Class', # Subjects here
                'Hi yeasin join the class here and \n code is ' + code + ' get now', # Body Messages
                settings.EMAIL_HOST_USER, # email sender
                [email], # to reciever email 
                fail_silently=False,
            )
            messages.success('Email has Sent') 
            return redirect('teacher')
            
        else:
            return HttpResponse ('Hey that an error')    
        '''       
