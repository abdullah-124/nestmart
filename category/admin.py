from django.contrib import admin
from .models import Product_category,Sub_Category
# Register your models here.
class Product_Category_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = [field.name for field in Product_category._meta.fields if field.name != "id"]
    
    
# regiter
admin.site.register(Product_category,Product_Category_Admin)
admin.site.register(Sub_Category)