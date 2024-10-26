from django.urls import path
from .views import user_register,user_login,check_username,varificaton_msg,user_logout

urlpatterns = [
    path('register/',user_register, name='register'),
    path('register/check-username/', check_username, name='check_username'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('varification/', varificaton_msg, name ='varification_msg')
]
