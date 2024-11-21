from django.shortcuts import render

# Create your views here.
def  wishlist(req):
    return render(req,'wishlist.html')