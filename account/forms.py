from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = MyUser
        fields = ('country_list', 'first_name', 'last_name', 'birthday', 'month_of_birth', 'year_of_birth', 'username',
                  'email', 'password1', 'password2', 'news_and_info', 'privacy_policy')


# from django.contrib.auth.models import User
# from django import forms
# from .models import UserExtended
#
#
# class UserForm(forms.ModelForm):
#     email = forms.CharField(max_length=100, required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'placeholder': '*Отображаемое имя'})
#         # self.fields['password'].widget.attrs.update({'placeholder': '*Пароль'})
#         self.fields['first_name'].widget.attrs.update({'placeholder': '*Имя'}, required=True)
#         self.fields['last_name'].widget.attrs.update({'placeholder': '*Фамилия'}, required=True)
#         # self.fields['email'].widget.attrs.update({'placeholder': '*Адрес электронной почты'}, required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'first_name', 'last_name', 'email')
#
#
# class UserExtendedForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['avatar'].widget.attrs.update({'placeholder': 'Аватар'})
#         self.fields['country_list'].widget.attrs.update({'placeholder': '*Страна'})
#         self.fields['birthday'].widget.attrs.update({'placeholder': '*День рождения'})
#         self.fields['month_of_birth'].widget.attrs.update({'placeholder': '*Месяц'})
#         self.fields['year_of_birth'].widget.attrs.update({'placeholder': '*Год'})
#         self.fields['news_and_info'].widget.attrs.update({'placeholder': 'информация'})
#         self.fields['privacy_policy'].widget.attrs.update({'placeholder': 'политика'}, required=True)
#
#     class Meta:
#         model = UserExtended
#         fields = ('avatar', 'country_list', 'birthday', 'month_of_birth', 'year_of_birth', 'news_and_info',
#                   'privacy_policy',)
