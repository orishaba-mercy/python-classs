from django.contrib import admin

from .models import Shipments
class ShipmentsAdmin(admin.ModelAdmin):
    list_display=("shipper_name","taxes_payments","cargo_description","image","date_depature","arrival_date","weight")
admin.site.register(Shipments, ShipmentsAdmin)






