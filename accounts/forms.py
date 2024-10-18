from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Coustomer

class RegestrationForm(UserCreationForm):
    mobileNum = forms.NumberInput(attrs={'placeholder':'enter '})
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password2','password1',]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your Password'}),
        }
class CoustomerForm(forms.ModelForm):
    class Meta: 
        model = Coustomer
        fields = ['mobile_num']
        widgets = {
            'mobile_num': forms.NumberInput(attrs={'placeholder': 'Enter your phone number'})
        }

