from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'result': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Grade'})
        }