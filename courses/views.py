from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course


def add(request):
    add = CourseForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/course/index')

    context = {
        'add': add
    }
    return render(request, 'course/add.html', context)


def index(request):
    index = Course.objects.all()
    context = {
        'index': index
    }

    return render(request, 'course/index.html', context)

def edit(request, id):
    edit_data = CourseForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/course/index')

    context = {
        'edit_data': edit_data
    }


    return render(request, 'course/edit.html', context)