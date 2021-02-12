from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add_student'),
    path('index/', views.index, name = 'show_student'),
    path('edit/<int:id>/', views.edit, name='edit_student'),

]