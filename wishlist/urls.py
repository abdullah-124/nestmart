from django.urls import path
from .views import wishlist
urlpatterns = [
    path('', wishlist, name='wishlist')
]
