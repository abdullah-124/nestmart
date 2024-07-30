from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from category.models import Product_category
# Create your views here.

def products(req):
    products = Product.objects.all()
    products_category = Product_category.objects.all()
    context = {
        'products': products,
        'product_category': products_category
    }
    return render(req, './products.html', context=context)

def product_details(req,id):
    product = Product.objects.get(id = id)
    
    return render(req, './product_details.html',{'product':product})