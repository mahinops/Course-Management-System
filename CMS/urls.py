from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('course/', include('courses.urls')),
    path('result/', include('result.urls')),
    path('notice/', include('notice.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)