from category.models import Sub_Category,Product_category

def load_nav_obj(req):
    context = dict()
    category = Product_category.objects.all()
    for i in category:  
        sub_category = Sub_Category.objects.filter(parent = i)
        context[i] = sub_category
    return {'category':context}