from django.contrib import admin
from .models import Coustomer

# Register your models here.
class CoustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Coustomer._meta.fields if field.name != "id"]
    
admin.site.register(Coustomer,CoustomerAdmin)