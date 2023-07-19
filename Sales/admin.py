from django.contrib import admin
from .models import Sales

# Register your models here.
class SalesAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price", "date_created")
admin.site.register(Sales, SalesAdmin)

