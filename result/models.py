from django.db import models
from courses.models import Course
from student.models import Student
from django.contrib import admin


class Result(models.Model):
    result_choice = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
        ('Not Published', 'Not Published'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    result = models.CharField(choices=result_choice, max_length=25)

    def __str__(self):
        return self.result


admin.site.register(Result)
