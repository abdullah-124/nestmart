from django.contrib import admin
from .models import Seller

# Register your models here.
class Seller_Admin(admin.ModelAdmin):
    # list_display = [field.name for field in Seller._meta.fields if field.name != "id"]
    list_display = ['store_name','user','total_product','sell_amount','rating']
    
admin.site.register(Seller,Seller_Admin)
