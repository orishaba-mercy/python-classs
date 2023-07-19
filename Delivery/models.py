from django.db import models

# Create your models here.
class Deliverys(models.Model):
    Customer_name=models.CharField(max_length=32)
    Delivery_adress=models.CharField(max_length=11)
    Delivery_method=models.CharField(max_length=12)
    Delivery_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Customer_name
