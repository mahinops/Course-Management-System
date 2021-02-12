from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='//')
def homepage(request):
    return render(request, 'base/base.html')
