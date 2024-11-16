from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.models import Coustomer
from .forms import EditForm

# Create your views here.
# USER PROFILE

# edit profile 
@login_required
def user_profile(req):
    user = req.user
    
    if(req.method == "POST"):
        form = EditForm(req, instance=user)
    
    else:
        form = EditForm(instance=user)
    return render(req, './user_profile.html', {'form':form})

# my orders
def my_orders(req):
    return render(req, './my_orders.html')