from django.db import models
from django.contrib.auth.models import User

# Create your models here.
START_RATING = (
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
)
class Review(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE) 
   text = models.TextField(null=True)
   rating = models.CharField(max_length=5, choices=START_RATING)