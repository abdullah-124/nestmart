from django.shortcuts import render
from category.models import Product_category,Sub_Category

# Create your views here.
def home(req):
    context = dict()
    category = Product_category.objects.all()
    for i in category:  
        sub_category = Sub_Category.objects.filter(parent = i)
        context[i.name] = sub_category

    # print(context)
    
    return render(req,'./home.html', {'category':context,'dumy': category})