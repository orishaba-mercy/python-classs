from django.db import models

class Orders(models.Model):
    customer_name=models.CharField(max_length=32)
    order_date=models.DateTimeField()
    total_amount=models.DecimalField(decimal_places=4,max_digits=4)
    delivery_adress=models.CharField(max_length=33)
    customer_contact=models.CharField(max_length=32)
    payment_status=models.BooleanField()
    # items_ordered=models.JSONField()
    order_status=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=32)