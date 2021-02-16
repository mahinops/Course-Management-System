from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def homepage(request):
    return render(request, 'base/base.html')

def login(request):
    return redirect('login/')
