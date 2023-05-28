from django import forms
from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'password1', 'password2']
