from django.urls import path
from .views import user_register,user_login

urlpatterns = [
    path('',user_register, name='register'),
    path('login/',user_login, name='login'),
]
