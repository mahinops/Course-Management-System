from django.db import models
from teacher.models import Teacher
from django.contrib import admin

class Notice(models.Model):
    title = models.CharField(max_length=500)
    notice_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

admin.site.register(Notice)