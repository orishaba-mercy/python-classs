from django.contrib import admin
from .models import Venders

# Register your models here.

class Venders_admin(admin.ModelAdmin):
  list_display=('first_name','last_name','email','Password','date_updated')

admin.site.register(Venders ,Venders_admin)


 