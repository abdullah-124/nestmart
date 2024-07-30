from django.db import models
from category.models import Product_category,Sub_Category
from origin.models import Origin,Brand
from seller.models import Seller
import math
# Create your models here.
PRODUCT_STATUS = (
    ('Out of stock','Out of stock'),
    ('Sale','Sale'),
    ('Upcomming', 'Upcomming'),
    ('Not available', 'Not available'),
    ('Deals of the day', 'Deals of the day'),
    ('Trending', 'Trending'),
)
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    category = models.ForeignKey(Product_category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    photo = models.ImageField(upload_to='images/product/prd')
    photo1 = models.ImageField(upload_to='images/product/prd',null=True, blank=True)
    photo2 = models.ImageField(upload_to='images/product/prd',null=True, blank=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    description = models.TextField()
    unit = models.CharField(max_length=10)
    discount = models.DecimalField(max_digits=3,decimal_places=1, default=0)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='Sale')
    mfg_date = models.DateField(null=True,blank=True)
    exp_date = models.DateField(null=True, blank=True)
    sold_quantity = models.IntegerField(default=0,null=True)
    origin = models.ForeignKey(Origin,on_delete=models.CASCADE,null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    total_review = models.IntegerField(default=0, null=True)
    rating = models.DecimalField(decimal_places=2,default=0.00,null=True,max_digits=3)
    created_at = models.DateTimeField(auto_now_add=True)
    @property 
    def current_price(self):
        return self.price - (self.price * self.discount)/100
    

    def __str__(self) -> str:
        return f'{self.category}/{self.name}'
    
    