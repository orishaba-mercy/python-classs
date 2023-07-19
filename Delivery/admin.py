from django.contrib import admin

# Register your models here.

from .models import Deliverys
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("Customer_name","Delivery_adress","Delivery_method","Delivery_date")
admin.site.register(Deliverys,DeliveryAdmin)

 