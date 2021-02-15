from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from .forms import UserForm
import hashlib
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/?next=/admin/')
def dashboard(request):
    user = User.objects.all()
    # user =request.user
    context = {
        'user': user
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='/admin/login/?next=/admin/')
def add(request):
    add = UserForm(request.POST or None)

    if add.is_valid():
        user = User.objects.create(
            username=add.cleaned_data.get('username'),
            email=add.cleaned_data.get('email'),
            is_staff=add.cleaned_data.get('is_staff'),
        )
        user.set_password(add.cleaned_data['password'])
        user.save()
        my_group = Group.objects.get(name=add.cleaned_data['groups'].first().name)
        my_group.user_set.add(user)
        return redirect('/dashboard')

    context = {
        'add': add
    }

    return render(request, 'dashboard/add.html', context)
