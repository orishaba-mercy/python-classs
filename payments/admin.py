from django.contrib import admin

from .models import Payments
class PaymentsAdmin(admin.ModelAdmin):
    list_display=("customer_name","total_amount","payment_status","order_status","payment_method")
admin.site.register(Payments,PaymentsAdmin)
