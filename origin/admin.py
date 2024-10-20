from django.contrib import admin
from .models import Location
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields if field.name != "id"]
    
admin.site.register(Location,LocationAdmin)