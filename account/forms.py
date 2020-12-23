from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from account.models import CustomUser


class CustomUserCreationForm (UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = CustomUser
        # fields = ('email', 'username', 'password1', 'password2')
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


# class AccountAuthenticationForm (forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')

#     def clean(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             password = self.cleaned_data['password']
#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError("invalid login")


# class AccountUpdateForm (forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username')

#     def clean_email(self):
#         if self.is_valid:
#             email = self.cleaned_data['email']
#             try:
#                 user= CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
#             except CustomUser.DoesNotExist:
#                 return email
#             raise forms.ValidationError('Email "%s" is already in use'%email)

#     def clean_username(self):
#         if self.is_valid:
#             username = self.cleaned_data['username']
#             try:
#                 user = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
#             except CustomUser.DoesNotExist:
#                 return username
#             raise forms.ValidationError('Username "%s" is already in use'%username)