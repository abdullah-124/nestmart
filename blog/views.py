from django.shortcuts import render

# Create your views here.
def blogs(req):
    return render(req,'./blogs.html')