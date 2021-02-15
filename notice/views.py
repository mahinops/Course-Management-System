from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/?next=/admin/')
def add(request):
    user = request.user
    add = NoticeForm(request.POST or None)

    if add.is_valid():
        add.save()
        return redirect('/notice/index')

    context = {
        'add': add,
        'user': user
    }

    return render(request, 'notice/add.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def index(request):
    index = Notice.objects.all()
    context = {
        'index': index
    }

    return render(request, 'notice/index.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def view_detail(request, id):
    detail = Notice.objects.get(id=id)
    context = {
        'detail': detail
    }
    return render(request, 'notice/view_detail.html', context)
