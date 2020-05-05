from django.db import models


# Create your models here.
class Student(models.Model):
    Stdno = models.IntegerField()
    Stdname = models.CharField(max_length=30)
    Profpic = models.FileField(blank=True, null=True)
    StdAdd = models.CharField(max_length=30)
