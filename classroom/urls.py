from django.urls import path
from .views.room import ViewClassRoom,SingleClass,CreateClassRoom,JoinRoom
from .views.people import PeopleUnderRoom

urlpatterns =[
    path('', ViewClassRoom.as_view(),name='all_class'),
    path('view/id/<int:id>', SingleClass.as_view(), name='single'),
    path('create/',CreateClassRoom.as_view(),name='create_class'),
    path('join/class/', JoinRoom.as_view(),name='join'),

    path('<int:id>/people/', PeopleUnderRoom.as_view(),name='people'),
]