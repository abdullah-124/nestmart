from django.shortcuts import render
from category.models import Product_category,Sub_Category

# Create your views here.
def home(req):
    # print(context)
    return render(req,'home.html')