from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups', 'email', 'is_staff', 'password']

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'groups': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Group'}),
        #     # 'is_staff': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Stuff?'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        # }

