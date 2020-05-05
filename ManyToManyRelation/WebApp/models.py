from django.db import models


# Create your models here
class Driver(models.Model):
    dname = models.CharField(max_length=25)

    def __str__(self):
        return self.dname


class Car(models.Model):
    cname = models.CharField(max_length=255, primary_key=True)
    drivers = models.ManyToManyField(Driver,)

    def __str__(self):
        return self.cname
