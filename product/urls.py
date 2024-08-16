from django.urls import path
from .views import products_load,filter_by_seller,ProductDetailView

urlpatterns = [
    path('', products_load, name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('category/<int:category_id>/', products_load, name='product_filter'),
    path('seller/<int:seller_id>/', filter_by_seller, name='filter_by_seller'),
]
