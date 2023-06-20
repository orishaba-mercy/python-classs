from django.contrib import admin

from .models import Orders
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer_name","order_date","total_amount","delivery_adress","customer_contact","payment_status","order_status","payment_method")
admin.site.register(Orders, OrderAdmin)