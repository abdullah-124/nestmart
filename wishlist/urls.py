from django.urls import path
from .views import wishlist,WishlistView
urlpatterns = [
    path('', WishlistView.as_view(), name='wishlist')
]
