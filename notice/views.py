from django.shortcuts import render
from . forms import NoticeForm
from .models import  Notice

def add(request):
    add = NoticeForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/notice/index')

    context = {
        'add' : add
    }

    return render(request, 'notice/add.html', context)


def index(request):
    index = Notice.objects.all()
    context = {
        'index': index
    }

    return  render(request, 'notice/index.html', context)