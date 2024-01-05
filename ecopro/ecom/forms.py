from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
        username = forms.CharField(max_length=50)
        password = forms.CharField(max_length=50)  
        

class SignupForm(UserCreationForm):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','password']