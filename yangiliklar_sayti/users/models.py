from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
