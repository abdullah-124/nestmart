from django.db import models

# Create your models here.
class Product_category(models.Model):
    name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField(max_length=30)
    image = models.ImageField(upload_to='images/category/')
    parent_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/category/sub_cat/',null=True,)
    parent = models.ForeignKey(Product_category,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name}"
    