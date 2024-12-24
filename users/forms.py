from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
