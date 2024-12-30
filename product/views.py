from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from .models import Product
from seller.models import Seller
from category.models import Product_category
from wishlist.models import Wishlist
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = super().get_object()
        context['product'] = product
        context['similar_product'] = Product.objects.filter(category = product.category).exclude(id=product.id)[:6]
        context['in_wishlist'] = Wishlist.objects.filter(user = self.request.user,product = product).exists()
        # product.view_count = product.view_count + 1 
        # product.save(update_fields=['view_count'])  
        # product.refresh_from_db()  
        return context