from dataclasses import fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import   UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
        
        
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        

