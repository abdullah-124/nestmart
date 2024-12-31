from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView
import json
from product.models import Product
from .models import Wishlist

# Create your views here.
def  wishlist(req):
    return render(req,'wishlist.html')

class WishlistView(LoginRequiredMixin,TemplateView):
    template_name = 'wishlist.html'
    login_url = '/accounts/login'
    redirect_field_name = 'home' 
    # get function for wishlist
    def get(self, req, *args, **kwargs):
        wishlist_items = Wishlist.objects.select_related('product').filter(user=req.user)
        return render(req, 'wishlist.html', )
        
    # add product to wishlist 
    def post(self, req, *args, **kwargs):
        try:
            # print(req.body)
            data = req.body.decode('utf-8')
            jsondata = json.loads(data)
            product_id  = jsondata.get('product_id')
            if not product_id:
                return JsonResponse({'type':'danger','messages': 'Product id is missing'})
            product = get_object_or_404(Product, id = product_id)
            wishlist,created = Wishlist.objects.get_or_create(
                user = self.request.user,
                product = product
            )
            if created:
                return JsonResponse({'type': 'success','message': 'Product added to wishlist'}, status=201)
            return JsonResponse({'type': 'info','message': 'Product already in wishlist'}, status=200)
        except Exception as e:
            return JsonResponse({'type':'danger', 'messages': str(e)})

@login_required
def wishlist_delete_view(req, id):
    # print(id)
    item = get_object_or_404(Wishlist, id = id)
    # print(item.user, item.product)
    if(item.user == req.user):
        item.delete()

    else :
        return render(req, 'common/not_found.html')
    return redirect('wishlist')
