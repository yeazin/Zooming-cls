from django.contrib import admin
from .models import ClassFiles, ClassRoom, MemberShip, RoomStream, Comment

admin.site.register(ClassRoom)
admin.site.register(ClassFiles)
admin.site.register(MemberShip)
admin.site.register(RoomStream)
admin.site.register(Comment)
