from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from product.models import Product

from .models import Wishlist

# Create your views here.
def  wishlist(req):
    return render(req,'wishlist.html')
class WishlistView(View):
    def get(self, req, *args, **kwargs):
        wishlist_items = Wishlist.objects.select_related('product').filter(user=req.user)
        context = {
            'wishlist_items': wishlist_items
        }
        return render(req, 'wishlist.html', context)
    def post(self,req, *args, **kwargs):
        product_id = req.POST.get('product_id')
        print('HELLLOOOO!!! ', product_id)
        if not product_id:
            return JsonResponse({"massage":"Product Dose not Exist"},status=204)
        product = get_object_or_404(Product, product_id)
        wishlist,created = Wishlist.objects.get_or_create(
            user = req.user,
            product = product
        )
        if created:
            return JsonResponse({'message': 'Product added to wishlist'}, status=201)
        return JsonResponse({'message': 'Product already in wishlist'}, status=200)