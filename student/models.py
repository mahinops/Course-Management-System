from django.db import models
from courses.models import Course
from django.contrib import admin


class Student(models.Model):
    department_choice = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('BBA', 'BBA')
    )
    blood_group_choice = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Inra', 'Inra'),
        ('Bombay', 'Bombay'),
        ('Gold', 'Gold'),
    )
    name = models.CharField(max_length=255)
    department = models.CharField(choices=department_choice, max_length=15)
    registration = models.CharField(max_length=25)
    roll = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=25)
    blood_group = models.CharField(choices=blood_group_choice, max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


admin.site.register(Student)
