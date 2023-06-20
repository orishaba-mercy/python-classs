from django.db import models

class Payments(models.Model):
    customer_name=models.CharField(max_length=32)
    total_amount=models.DecimalField(decimal_places=4,max_digits=4)
    payment_status=models.BooleanField()
    order_status=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=32)

