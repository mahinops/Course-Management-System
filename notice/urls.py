from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add_notice'),
    path('index/', views.index, name = 'show_notice'),
    path('detail/<int:id>/', views.view_detail, name = 'view_detail'),

]