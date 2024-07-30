from django.urls import path
from .views import products,product_details

urlpatterns = [
    path('', products, name='products'),
    path('<int:id>/', product_details, name='product_details'),
]
