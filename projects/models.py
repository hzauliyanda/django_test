from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()

