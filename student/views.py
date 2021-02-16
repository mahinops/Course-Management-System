from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add(request):
    user = request.user
    add = StudentForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/student/index')

    context = {
        'add' : add,
        'user': user,
    }
    return render(request, 'student/add.html', context)


@login_required(login_url='/')
def index(request):
    index = Student.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'student/index.html', context)

@login_required(login_url='/')
def edit(request, id):
    user = request.user
    edit_data = StudentForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/student/index')

    context = {
        'edit_data': edit_data,
        'user': user,
    }


    return render(request, 'student/edit.html', context)