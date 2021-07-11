
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('profiles.urls')),
    path('class/', include('classroom.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)