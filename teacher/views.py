from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add(request):
    user = request.user
    add = TeacherForm(request.POST or None)


    if add.is_valid():
        add.save()
        return redirect('/teacher/index')

    context = {
        'add' : add,
        'user': user
    }
    return render(request, 'teacher/add.html', context)


@login_required(login_url='/')
def index(request):
    index = Teacher.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'teacher/index.html', context)

@login_required(login_url='/')
def edit(request, id):
    user = request.user
    edit_data = TeacherForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/teacher/index')

    context = {
        'edit_data': edit_data,
        'user': user,
    }


    return render(request, 'teacher/edit.html', context)
