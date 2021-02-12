from django.db import models
from django.contrib import admin


class Teacher(models.Model):
    department_choice = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('BBA', 'BBA'),
    )
    name = models.CharField(max_length=255)
    department = models.CharField(choices=department_choice, max_length=15)
    designation = models.CharField(max_length=55)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name

admin.site.register(Teacher)
