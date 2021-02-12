from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice


def add(request):
    add = NoticeForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/notice/index')

    context = {
        'add': add
    }

    return render(request, 'notice/add.html', context)


def index(request):
    index = Notice.objects.all()
    context = {
        'index': index
    }

    return render(request, 'notice/index.html', context)


def view_detail(request, id):
    detail = Notice.objects.get(id=id)
    context = {
        'detail': detail
    }
    return render(request, 'notice/view_detail.html', context)
