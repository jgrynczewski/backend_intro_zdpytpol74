from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    city = models.CharField(max_length=50)
