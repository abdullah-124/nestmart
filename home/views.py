from django.shortcuts import render
from category.models import Product_category,Sub_Category
from product.models import Product
# Create your views here.
def home(req):
    products = Product.objects.all()
    popular_products = Product.objects.all().order_by('discount','-view_count')[:10]
    context = {
        'popular_products': popular_products
    }
    return render(req,'home.html', context=context)