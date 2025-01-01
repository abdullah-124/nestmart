from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_page(req):
    return render(req, 'cart_page.html')