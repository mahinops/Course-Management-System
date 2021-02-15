from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission, _user_has_perm


@login_required(login_url='/admin/login/?next=/admin/')
def add(request):
    user = request.user
    # if user.groups.name == 'teacher':

    add = CourseForm(request.POST or None)
    if add.is_valid():
        add.save()
        return redirect('/course/index')

    context = {
        'add': add,
        'user': user,

    }
    return render(request, 'course/add.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def index(request):
    index = Course.objects.all()
    context = {
        'index': index
    }

    return render(request, 'course/index.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def edit(request, id):
    user = request.user
    edit_data = CourseForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/course/index')

    context = {
        'edit_data': edit_data,
        'user': user,
    }


    return render(request, 'course/edit.html', context)