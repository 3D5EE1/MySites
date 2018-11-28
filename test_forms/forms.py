from django.core.validators import URLValidator
from django.forms import ModelForm
from django import forms
from .models import Author, Article


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'text']


class ContactForm(forms.Form):
    boolean_field = forms.NullBooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label='Введите ваше имя')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    sender = forms.EmailField(label='Введите ваш емеил!')


# def validate_url(value):
#     validation_url = URLValidator()
#     value_one_invalid = False
#     value_two_invalid = False
#     try:
#         validate_url(value)
#     except:
#         value_one_invalid = True
#
#     value_two_url = 'http://' + value
#     try:
#         validate_url(value_two_url)
#     except:
#         value_two_invalid = True
#
#     if value_one_invalid == False and value_two_invalid == False:
#         raise forms.ValidationError('Неправильый адрес сайта!')
#     return value


class UrlForm(forms.Form):
    title = forms.CharField(label='Название сайта')
    url = forms.CharField(label='Адрес сайта',)  # validators=[validate_url])

    def clean(self):
        cleaned_date = super(UrlForm, self).clean()

    def clean_url(self):
        url = self.cleaned_data['url']
        validation_url = URLValidator()
        try:
            validation_url(url)
        except:
            raise forms.ValidationError('Это не адрес сайта')
        return url
