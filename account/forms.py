from django.contrib.auth.models import User
from django import forms
from .models import UserExtended


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserExtendedForm(forms.ModelForm):

    class Meta:
        model = UserExtended
        fields = ('avatar', 'country_list', 'birthday', 'month_of_birth', 'year_of_birth', 'news_and_info',
                  'privacy_policy',)
