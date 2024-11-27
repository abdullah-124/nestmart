from django.db import models
from category.models import Product_category

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/brand/',null=True)
    product_type = models.ManyToManyField(Product_category)
    contact_num =models.CharField(max_length=13)
    email = models.EmailField()
    total_rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    
    