from django.shortcuts import render
from .forms import ResultForm
from .models import  Result


def add(request):
    add = ResultForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/result/index')

    context = {
        'add': add
    }

    return  render(request, 'result/add.html', context)


def index(request):
    index = Result.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'result/index.html', context)