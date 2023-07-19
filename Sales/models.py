from django.db import models
# Create your models here.
class Sales(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=9,decimal_places=0)
    description=models.TextField()
    image=models.ImageField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()
