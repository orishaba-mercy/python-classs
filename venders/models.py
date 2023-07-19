from django.db import models


# Create your models here.
class Venders(models.Model):
   
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    Password=models.CharField(max_length=8)
    date_updated=models.DateTimeField(auto_now=True)








