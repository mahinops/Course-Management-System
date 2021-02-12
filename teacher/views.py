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
    index = Teacher.objects.get(id=id)
    context = {
        'index': index
    }
    return render(request, 'teacher/edit.html', context)
