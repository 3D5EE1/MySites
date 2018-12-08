from django.contrib.auth.models import User
from django import forms
from .models import Account


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('avatar', 'country_list', 'birthday', 'month_of_birth', 'year_of_birth', 'privacy_policy',)