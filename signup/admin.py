from django.contrib import admin
from.models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
 list_display=("first_name","last_name","email","password","image")

admin.site.register(Signup, SignupAdmin)
    

