from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom,RoomStream
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create Stream
class CreateStream(View):
    method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        

    def post(self,request,id):
        user = request.user
        room = get_object_or_404(ClassRoom,id=id)
        post = request.POST.get('post')

        stream = RoomStream(user=user,room=room,post=post)
        stream.save()
        messages.success(request,'The Stream has Been Added')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        