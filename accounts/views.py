from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import RegestrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def user_register(req):
    if(req.method == 'POST'):
        form = RegestrationForm(req.POST)
        if(form.is_valid()):
            print("data found")
            print(form.cleaned_data)
            user = form.save()
            login(req, user)
            return JsonResponse({
                "code":"200",
                "massage":"Account Created Successfull",
                "username": form.cleaned_data['username'],
                "email": form.cleaned_data['email'],
                })
    else :
        print('data not found')
        form = RegestrationForm()
    return render(req,'accounts/register.html', {'form':form})

# user login
def user_login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(username = username, password = password)
    if(user):
        login(req,user)
        return JsonResponse({"username":user.username})
    return render(req,'accounts/login.html')