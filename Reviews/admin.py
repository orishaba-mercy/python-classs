from django.contrib import admin

# Register your models here.
from .models import Reviews
class ReviewsAdmin(admin.ModelAdmin):
  list_display=("customer_name","product_name","rating","image","review_date"," review_text")
admin.site.register(Reviews.ReviewsAdmin)




    

    
