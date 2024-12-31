from django.urls import path
from .views import WishlistView,wishlist_delete_view
urlpatterns = [
    path('', WishlistView.as_view(), name='wishlist'),
    path('<int:id>/delete', wishlist_delete_view, name='delete_wishlist')
]
