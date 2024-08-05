from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = 'username', 'password1', 'password2'


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password = forms.CharField(label='password', widget=forms.PasswordInput())





