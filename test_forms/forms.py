from django.forms import ModelForm
from django import forms
from .models import Author, Article


class AuthorOneForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'text']


class ContactForm(forms.Form):
    boolean_field = forms.BooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label='Введите ваше имя')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    sender = forms.EmailField(label='Введите ваш емеил!')


