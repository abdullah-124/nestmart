from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import RegestrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Coustomer

# Create your views here.
def user_register(req):
    print('helllo')
    if(req.method == 'POST'):
        form = RegestrationForm(req.POST)
        if(form.is_valid()):
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(password1,password2)
            if(password1 == password2):
                user = form.save(commit=True)
                # user.is_active = False
                # user.save()
                login(req,user=user)
                print(user)
                messages.success(req, 'Registration successful! Please check your email to verify your account.')
                return redirect('register')
            else:
                messages.error(req, "Passowrd does't match")
        else :
            for error in form.errors.values():
                messages.error(req, error)
    else :
        print('----***----')
        form = RegestrationForm()
    return render(req,'accounts/register.html', {'form':form})

# user login
def user_login(req):
    print('loin')
    username = req.POST.get('username')
    password = req.POST.get('password')
    print(username,password)
    user = authenticate(username = username, password = password)
    if(user):
        login(req,user)
        previous_url = req.META.get('HTTP_REFERER', '/')
        return redirect('home')
    return render(req,'accounts/login.html')
# USER LOGOUT
def user_logout(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('home')
    return redirect('login')

# username check exist or not
def check_username(request):
    username = request.GET.get('username', None)
    # print(username)
    if username:
        exists = Coustomer.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

def varificaton_msg(req):
    return render(req,'./varification_msg.html')
