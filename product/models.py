from django.db import models
from datetime import date
from category.models import Product_category,Sub_Category
from review.models import Review
from origin.models import Location,Brand
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
DELEVERY_MASSAGE = 'Delevery need to 2 hour for local items, 7 working days for thus items thats deleverd from outside of you city'
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    category = models.ForeignKey(Product_category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    photo = models.ImageField(upload_to='images/product/prd')
    photo1 = models.ImageField(upload_to='images/product/prd',null=True, blank=True)
    photo2 = models.ImageField(upload_to='images/product/prd',null=True, blank=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE, related_name='products')
    stock_quantity = models.IntegerField()
    description = models.TextField()
    short_description = models.CharField(max_length=150, blank=True, null=True)
    unit = models.CharField(max_length=10)
    discount = models.DecimalField(max_digits=3,decimal_places=1, default=0)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='Sale')
    mfg_date = models.DateField(null=True,blank=True, default=date.today)
    exp_date = models.DateField(null=True, blank=True)
    sold_quantity = models.PositiveIntegerField(default=0,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    total_review = models.IntegerField(default=0, null=True)
    review_count = models.IntegerField(default=0,null=True)
    view_count = models.PositiveIntegerField(default=0,null=True)
    delevery_massage = models.TextField(default=DELEVERY_MASSAGE, null = True)
    # local_delevery = models.BooleanField(default=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property 
    def current_price(self):
        res =  self.price - (self.price * self.discount)/100
        return round(res,2)
    @property
    def avg_rating(self):
        res = self.total_review/self.review_count
        return round(res,1)
        
    class Meta:
        ordering = ['sub_category']
    def __str__(self) -> str:
        return f'{self.category}/{self.name}'
    
    