from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Coustomer

class RegestrationForm(UserCreationForm):
    class Meta:
        model = Coustomer
        fields = ['user']

