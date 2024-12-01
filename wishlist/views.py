from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Wishlist

# Create your views here.
def  wishlist(req):
    return render(req,'wishlist.html')
class WishlistView(LoginRequiredMixin,View):
    def get(self, req, *args, **kwargs):
        wishlist_items = Wishlist.objects.select_related('product').filter(user=req.user)
        context = {
            'wishlist_items': wishlist_items
        }
        return render(req, 'wishlist.html', context)
