from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    birth_date = models.DateField()
    age = models.IntegerField()