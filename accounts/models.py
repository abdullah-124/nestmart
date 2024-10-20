from django.db import models
from django.contrib.auth.models import User,AbstractUser
from origin.models import Location

# Create your models here.
class Coustomer(AbstractUser):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Location,null=True, blank=True, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=13,null=True)
    photo = models.ImageField(upload_to='image/coustomer/',null=True,blank=True)
    total_point = models.IntegerField(default=0)
    total_spend = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.username
    