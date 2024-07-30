from django.db import models
from django.contrib.auth.models import User
from origin.models import Origin

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='images/seller/')
    mobile = models.CharField(max_length=12)
    total_product = models.IntegerField(default=0,null=True)
    product_sell = models.IntegerField(default=0,null=True)
    sell_amount = models.IntegerField(default=0,null=True)
    rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00,null=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return f"{self.user.username}/{self.store_name}"