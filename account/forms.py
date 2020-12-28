from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from account.models import CustomUser


class CustomUserCreationForm (UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
