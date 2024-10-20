from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Coustomer

class RegestrationForm(UserCreationForm):
    mobileNum = forms.NumberInput(attrs={'placeholder':'enter '})
    class Meta:
        model = Coustomer
        fields = ['username','email', 'mobile_num', 'password2','password1',]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your Password'}),
        }
