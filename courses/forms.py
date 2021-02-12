from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Code'}),
            'teacher': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Teacher'})
        }