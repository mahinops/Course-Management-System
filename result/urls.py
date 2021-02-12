from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add_result'),
    path('index/', views.index, name = 'show_result')
]