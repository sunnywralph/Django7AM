from django.db import models

# Create your models here.
class document(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    wallpaper = models.ImageField(upload_to='wall/')