from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=12)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    def register(self):
        self.save
        def get_customer_by_email(email):
            try:
                return Customer.objects.get(email=email)
            except:
                return False
        def isExist(self):
                if Customer.objects.filter(email = self.email):
                    return True
                return False









