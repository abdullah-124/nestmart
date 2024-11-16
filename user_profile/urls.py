from django.urls import path
from .views import user_profile,my_orders

urlpatterns = [
    path('',user_profile, name='user_profile'),
    path('my_orders/', my_orders, name='my_orders'),
]
