from django.db import models

# Create your models here.
class Regestration(models.Model):
    First_name=models.CharField(max_length=10)
    Last_name=models.CharField(max_length=8)
    Email=models.EmailField(max_length=20)
    PassWord=models.CharField(max_length=10)
    def __str__(self):
        return self.First_name
