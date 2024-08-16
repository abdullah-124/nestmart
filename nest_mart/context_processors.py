from django.db.models import Count
from category.models import Sub_Category,Product_category
from seller.models import Seller

def load_nav_obj(req):
    context = dict()
    category = Product_category.objects.all()
    seller = Seller.objects.annotate(total_product = Count('products')).order_by('-total_product')
    for i in category:  
        sub_category = Sub_Category.objects.filter(parent = i)
        context[i] = sub_category
    return {'category':context, 'seller':seller}