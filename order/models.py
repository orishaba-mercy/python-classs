from django.db import models
from cart .models import Cart
from customer .models import Customer
from Delivery.models import Deliverys

class Orders(models.Model):
    basket=models.ManyToManyField(Cart)
    customers=models.OneToOneField(Customer,null=True,on_delete=models.CASCADE)
    shipment=models.ForeignKey(Deliverys,on_delete=models.CASCADE,null=True)
    
    customer_name=models.CharField(max_length=32)
    order_date=models.DateTimeField()
    total_amount=models.DecimalField(decimal_places=4,max_digits=4)
    delivery_adress=models.CharField(max_length=33)
    customer_contact=models.CharField(max_length=32)
    payment_status=models.BooleanField()
    order_status=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=32)