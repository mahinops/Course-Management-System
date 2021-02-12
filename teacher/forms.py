from django import forms
from .models import *

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher Name'}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }
