from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Coustomer
from .forms import EditForm

# Create your views here.
# USER PROFILE

# edit profile 
@login_required
def user_profile(req):
    user = req.user
    update_status = None
    photo_removed = req.POST.get('photo_removed')
    if(req.method == "POST"):
        form = EditForm(req.POST, req.FILES, instance=user)
        if(form.is_valid()):
            user = req.user
            if(photo_removed):
              user.photo.delete(save=False)
              user.photo = None
              user.save()
              update_status = True
            if form.has_changed():
                form.save()  
                # print('updated...   ')
                update_status = True
        else:
            update_status = False
    else:
        form = EditForm(instance=user)
    
    return render(req, './user_profile.html', {'form':form,'update_status':update_status})

# my orders
def my_orders(req):
    return render(req, './my_orders.html')