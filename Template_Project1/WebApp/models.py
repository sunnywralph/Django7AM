from django.db import models
# Create your models here.
class Emp(models.Model):
    EmpId = models.IntegerField()
    EmpName = models.CharField(max_length=40)
    EmpSal = models.IntegerField()
    EmpAdd = models.CharField(max_length=40)