from django.db import models

# Create your models here.
class Signup(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.ImageField()

