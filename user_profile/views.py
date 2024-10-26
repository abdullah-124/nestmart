from django.shortcuts import render

# Create your views here.
# USER PROFILE
def user_profile(req):
    return render(req, './user_profile.html')