from django.contrib import admin
from .models import Coustomer

# Register your models here.
class CoustomerAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_staff','mobile_num']
    
admin.site.register(Coustomer,CoustomerAdmin)