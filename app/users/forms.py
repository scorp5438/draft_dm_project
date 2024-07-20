from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserloginForm(AuthenticationForm):
    class Meta:
        model = User

# from .models import User
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email', 'company', 'post')  # Добавьте свои поля
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User
#         fields = ('username', 'email', 'company', 'post')  # Добавьте свои поля
