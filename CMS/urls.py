from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('course/', include('courses.urls')),
    path('result/', include('result.urls')),
    path('notice/', include('notice.urls')),
]
