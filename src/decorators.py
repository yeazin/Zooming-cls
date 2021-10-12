'''
Custom Decorators for App
'''
from django.shortcuts import redirect,get_object_or_404
from functools import wraps
# importing models
from classroom.models import ClassRoom,MemberShip
from profiles.models import Student

'''
This custom decorators functions are below:
- decorator will check if student has the access to the class
- if has the access then student can join otherwise it will show an error 403
'''
def SingleClassForbidden(view_func):
    @wraps(view_func)
    def wrapper(request,id,*args,**kwargs):

        try:
            if request.user.students:
                room = get_object_or_404(ClassRoom,id=id)
                check = MemberShip.objects.filter(room = room, student=request.user.students)
                if check :
                    return view_func(request,id,*args,**kwargs)
                else:
                    return redirect('/') 
        except Student.DoesNotExist:
            return view_func(request,id,*args,**kwargs)

    return wrapper