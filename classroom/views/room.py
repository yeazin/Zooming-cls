from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom, MemberShip
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


#create classroom
class CreateClassRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        context ={

        }
        return render(request,'class/create_class.html', context)
    
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
class SingleClass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        room = get_object_or_404(ClassRoom  ,id=id) 
        context ={
            'room':room,
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
            if user.member.is_join == True:
                messages.success(request,'You are Already a member')
                return redirect('single', id=check_code.id )
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
    pass