from django.db import models
from django.contrib.auth.models import User,AbstractUser
from origin.models import Location

# Create your models here.
ROLE_CHOICES = (
    ('admin','Admin'),
    ('seller','Seller'),
    ('customer','Customer'),
)
# 
class Coustomer(AbstractUser):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer', null=True,blank=True)
    address = models.ForeignKey(Location,null=True, blank=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,null=True,blank= True)
    mobile_num = models.CharField(max_length=13,null=True)
    photo = models.ImageField(upload_to='image/coustomer/',null=True,blank=True)
    total_point = models.IntegerField(default=0)
    total_spend = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.username
    