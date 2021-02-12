from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add_teacher'),
    path('index/', views.index, name= 'show_teacher'),
    path('edit/<int:id>', views.edit)
]