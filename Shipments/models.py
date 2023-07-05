from django.db import models

# Create your models here.
class Shipments(models.Model):
    shipper_name=models.CharField(max_length=40)
    taxes_payments=models.DecimalField(max_digits=10,decimal_places=2)
    cargo_description=models.TextField()
    image=models.ImageField()
    date_depature=models.DateTimeField(auto_now_add=True)
    arrival_date=models.DateTimeField(auto_now=True)
    weight=models.PositiveIntegerField()
