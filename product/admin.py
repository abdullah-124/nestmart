from django.contrib import admin
from .models import Product
# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','category','seller')}
    # list_display = [field.name for field in Product._meta.fields if field.name != "id"]
    list_display = ['name','seller','current_price','unit','status','rating']
        
    
admin.site.register(Product, ProductModelAdmin)