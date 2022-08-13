from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    # user_name = forms.CharField(label = 'user_name')
    email     = forms.EmailField(label='email')
    password1 = forms.CharField(label='password1')
    password2 = forms.CharField(label='password2')


    class Meta:
        model = User
        fields = ['email','username','password1','password2']