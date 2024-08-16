from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from .models import Product
from seller.models import Seller
from category.models import Product_category
# Create your views here.

def products_load(req, category_id=None):
    products = Product.objects.all()
    # category
    try:
        if category_id:
            category = get_object_or_404(Product_category, id=category_id)
            products = products.filter(category=category)
        else:
            category = None
    except Http404:
        return render(req, './products.html')   
    
    # sort by 
    sort_by = req.GET.get('sort_by')
    # print(sort_by)
    if(sort_by):
        products = products.order_by(sort_by)
    
    context = {
        'products': products,
        'sort_by': sort_by,
    }
    return render(req, './products.html', context=context)

def filter_by_seller(req,seller_id = None):
    seller = Seller.objects.get(id=seller_id)
    products = Product.objects.filter(seller=seller)

    products_load(req)
    
    return render(req, './products.html',{'products':products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'

    def get_object(self):
        product = super().get_object()
        # view count
        # product.view_count = product.view_count + 1 
        # product.save(update_fields=['view_count'])  
        # product.refresh_from_db()  
        return product