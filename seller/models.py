from django.db import models
from django.contrib.auth.models import User
from origin.models import Location
from accounts.models import Coustomer
from django.conf import settings

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(Coustomer,on_delete=models.CASCADE)
    # coustomer = models.OneToOneField(Coustomer, on_delete=models.CASCADE,null=True,blank=True)
    store_name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='images/seller/')
    cover_photo = models.ImageField(upload_to='images/seller/', null=True, blank=True)
    mobile = models.CharField(max_length=12)
    product_sell = models.IntegerField(default=0,null=True)
    sell_amount = models.IntegerField(default=0,null=True)
    total_review = models.IntegerField(default=0, null=0)
    review_count = models.IntegerField(default=0,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def total_product(self):
        return self.products.count()
    def __str__(self) -> str:
        return f"{self.user.username}/{self.store_name}"
    def save(self, *args, **kwargs):
        if(not self.location and self.user.location):
            self.location, created = Location.objects.get_or_create(name=self.user.location)
            super().save(*args, **kwargs)
        super(Seller, self).save(*args, **kwargs)