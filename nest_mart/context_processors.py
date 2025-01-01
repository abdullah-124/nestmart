from django.db.models import Count
from category.models import Sub_Category,Product_category
from seller.models import Seller
from wishlist.models import Wishlist

def load_nav_obj(req):
    print(req.user)
    context = dict()
    category = Product_category.objects.all()
    seller = Seller.objects.annotate(total_product = Count('products')).order_by('-total_product')
    wishlist = []
    if req.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=req.user)
    for i in category:  
        sub_category = Sub_Category.objects.filter(parent = i)
        context[i] = sub_category
    return {'category':context, 'seller':seller,'wishlist': wishlist}