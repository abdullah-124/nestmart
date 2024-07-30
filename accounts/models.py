from django.db import models
from django.contrib.auth.models import User
from origin.models import Origin

# Create your models here.
class Coustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ManyToManyField(Origin)
    total_point = models.IntegerField(default=0)
    total_spend = models.IntegerField(default=0)
    