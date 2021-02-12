from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add(request):
    add = StudentForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/student/index')

    context = {
        'add' : add
    }
    return render(request, 'student/add.html', context)


def index(request):
    index = Student.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'student/index.html', context)

def edit(request, id):
    edit_data = StudentForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/student/index')

    context = {
        'edit_data': edit_data
    }


    return render(request, 'student/edit.html', context)