from django.urls import path
from .views import seller_profile,all_seller

urlpatterns = [
    path('', view=all_seller, name='seller'),
    path('<int:id>/', view=seller_profile, name='seller_profile')
]
