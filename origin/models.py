from django.db import models
from category.models import Product_category

# Create your models here.
class Origin(models.Model):
    address = models.CharField(max_length=50,)
    postal = models.IntegerField()
    district = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default="Bangladesh")
    def __str__(self) -> str:
        return f"{self.address},{self.postal},{self.city}"

class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/brand/',null=True)
    product_type = models.ManyToManyField(Product_category)
    contact_num =models.CharField(max_length=13)
    email = models.EmailField()
    total_rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    
    