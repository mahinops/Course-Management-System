from django.shortcuts import render, redirect
from .forms import ResultForm
from .models import Result
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/?next=/admin/')
def add(request):
    user = request.user
    add = ResultForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/result/index')

    context = {
        'add': add,
        'user': user,
    }

    return render(request, 'result/add.html', context)


@login_required(login_url='/admin/login/?next=/admin/')
def index(request):
    index = Result.objects.all()
    context = {
        'index': index
    }

    return render(request, 'result/index.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def edit(request, id):
    user = request.user
    edit_data = ResultForm(request.POST)
    if edit_data.is_valid():
        edit_data.save()
        return redirect('/result/index')

    context = {
        'edit_data': edit_data,
        'user': user,
    }


    return render(request, 'result/edit.html', context)