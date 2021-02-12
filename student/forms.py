from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Department'}),
            'registration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration Number'}),
            'roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'blood_group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Blood Group'}),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Name'})
        }