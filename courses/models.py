from django.db import models
from teacher.models import Teacher
from django.contrib import admin


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=15)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

admin.site.register(Course)