from django.shortcuts import render, redirect
from .forms import ResultForm
from .models import Result


def add(request):
    add = ResultForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/result/index')

    context = {
        'add': add
    }

    return render(request, 'result/add.html', context)


def index(request):
    index = Result.objects.all()
    context = {
        'index': index
    }

    return render(request, 'result/index.html', context)

def edit(request, id):
    edit_data = ResultForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/result/index')

    context = {
        'edit_data': edit_data
    }


    return render(request, 'result/edit.html', context)