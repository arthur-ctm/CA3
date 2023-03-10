from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class LoginForm(AuthenticationForm):
    # Define the username field with a label of 'Username'
    # and a widget of TextInput with a class of 'form-control'
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Define the password field with a label of 'Password'
    # and a widget of PasswordInput with a class of 'form-control'
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class SignupForm(UserCreationForm):
    # Define the username field with a label of 'Username'
    # and a widget of TextInput with a class of 'form-control'
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Define the first password field with a label of 'Password'
    # and a widget of PasswordInput with a class of 'form-control'
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    # Define the second password field with a label of 'Password confirmation'
    # and a widget of PasswordInput with a class of 'form-control'
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    # Specify the User model to use for this form
    model = User

    # Specify the fields that will be included in the form
    fields = ('username', 'password1', 'password2')
