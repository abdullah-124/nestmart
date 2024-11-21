from django.db import models
from accounts.models import Coustomer
from product.models import Product

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(Coustomer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    added_at = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveIntegerField(default=1)
    class Meta: 
        unique_together = ('user','product')
        ordering = ['added_at']
    
    def __str__(self):
        return f"{self.user.username}/{self.product.name}"