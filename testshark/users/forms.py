from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _  # Import gettext_lazy

class SignupForm(UserCreationForm):
    """Custom signup form."""
    class Meta:
        model = User
        fields = ("username", "email",  "password1","password2")

class LoginForm(AuthenticationForm):
    """Custom login form."""
    username = forms.CharField(label=_("Username"), widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)