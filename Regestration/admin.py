from django.contrib import admin

# Register your models here.
from.models import Regestration
class RegestrationAdmin(admin.ModelAdmin):
    List_display=("First_name","Last_name","Email","PassWord")
admin.site.register(Regestration,RegestrationAdmin)

