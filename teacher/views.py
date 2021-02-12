from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher


def add(request):
    add = TeacherForm(request.POST or None)


    if add.is_valid():
        add.save()
        return redirect('/teacher/index')

    context = {
        'add' : add
    }
    return render(request, 'teacher/add.html', context)


def index(request):
    index = Teacher.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'teacher/index.html', context)


def edit(request, id):
    edit_data = TeacherForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/teacher/index')

    context = {
        'edit_data': edit_data
    }


    return render(request, 'teacher/edit.html', context)
