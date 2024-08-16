from django.db import models
from django.contrib.auth.models import User
from origin.models import Origin
from accounts.models import Coustomer

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    coustomer = models.OneToOneField(Coustomer, on_delete=models.CASCADE,null=True,blank=True)
    store_name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='images/seller/')
    mobile = models.CharField(max_length=12)
    product_sell = models.IntegerField(default=0,null=True)
    sell_amount = models.IntegerField(default=0,null=True)
    rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00,null=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, null=True)
    
    
    def total_product(self):
        return self.products.count()
    def __str__(self) -> str:
        return f"{self.user.username}/{self.store_name}"