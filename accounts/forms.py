from django import forms
from django.contrib.auth.models import User
from material import *

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput
        }

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput
        }