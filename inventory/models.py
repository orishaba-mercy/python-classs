from django.db import models
from venders.models import Venders
# Create your models here.
class Product(models.Model):
    Venders=models.ForeignKey(Venders,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    image=models.ImageField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()
