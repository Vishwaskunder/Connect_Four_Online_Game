# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']



from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']