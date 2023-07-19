from django.contrib import admin

# Register your models here.

from .models import Reviews

class Reviews_admin(admin.ModelAdmin):
  list_display=("customer_name","product_name","rating","image","review_date")
admin.site.register(Reviews, Reviews_admin)