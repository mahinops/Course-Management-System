from django.shortcuts import render
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