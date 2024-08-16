from django.shortcuts import render
from seller.models import Seller
from product.models import Product

# Create your views here.
def all_seller(req):
    sellers = Seller.objects.all()
    return render(req, 'all_seller.html', {'sellers':sellers})
def seller_profile(req,id):
    store = Seller.objects.get(id = id)
    products = Product.objects.filter(seller = store)
    context = {
        'store': store,
        'products': products
    }
    return render(req, 'seller_profile.html', context=context)