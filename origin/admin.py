from django.contrib import admin
from .models import Origin
# Register your models here.
class OrginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Origin._meta.fields if field.name != "id"]
    
admin.site.register(Origin,OrginAdmin)