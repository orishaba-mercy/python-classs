from django.db import models

# Create your models here.
class Reviews(models.Model):
    customer_name=models.CharField(max_length=40)
    product_name=models.TextField(max_length=10)
    rating=models.PositiveBigIntegerField()
    image=models.ImageField()
    review_text=models.TextField(max_length=40)
    review_date=models.DateTimeField(auto_now=True)
    

    
