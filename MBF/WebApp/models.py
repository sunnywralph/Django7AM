from django.db import models

#create your views here
class Emp(models.Model):
	Name = models.CharField(max_length=30)
	Salary = models.IntegerField()
