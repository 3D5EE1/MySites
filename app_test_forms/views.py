from django.shortcuts import render
from django.http import HttpResponse
from app_test_forms import forms
from django.views import generic
from django.views import View

# Create your views here.


def test_forms(request):
    return render(request, 'app_test_forms/test_forms.html')


def search(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            return HttpResponse(f'Вы хотели найти {request.GET["q"]}')
        else:
            return HttpResponse(f'Вы отправили пустую форму')


def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    birth = request.POST['birth']
    gender = request.POST['gender']
    with open('some.txt', 'w') as some_file:
        some_file.write(f'Имя: {name}\n')
        some_file.write(f'Фамилия: {surname}\n')
        some_file.write(f'Дата рождения: {birth}\n')
        some_file.write(f'Пол: {gender}\n')
    return HttpResponse('Данные были успешно записаны!')


# -------------------------------------------------------------------------------


# def form(request):
#     form_for_author = forms.AuthorForm
#     form_for_article = forms.ArticleForm
#     form_contact = forms.ContactForm
#     context = {
#         'form_for_author': form_for_author,
#         'form_for_article': form_for_article,
#         'form_contact': form_contact,
#     }
#     return render(request, 'app_test_forms/form.html', context)


def add_author(request):
    author_form = forms.AuthorForm(request.POST)
    result = f'Автор успешно добавлен {request.path}'
    if request.method == 'POST' and author_form.is_valid():
        data = author_form.cleaned_data
        author_form.save()
        print(data)
        return HttpResponse(result)


def add_article(request):
    article_form = forms.ArticleForm(request.POST)
    if request.method == 'POST' and article_form.is_valid():
        article_form.save()
        return HttpResponse('Статья добавления!')


class ContactFormView(View):

    form_for_author = forms.AuthorForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)
        context = {
            'form_for_author': self.form_for_author,
            'form_for_article': self.form_for_article,
            'form_contact': form,
        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request, 'app_test_forms/form.html', context)

    def get(self, request):
        context = {
            'form_for_author': self.form_for_author,
            'form_for_article': self.form_for_article,
            'form_contact': self.form_contact
        }
        return render(request, 'app_test_forms/form.html', context)


class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def get(self, request):
        context = {
            'form_url': self.form_submit_url
        }
        return render(request, 'app_test_forms/url_form.html', context)

    def post(self, request):
        form = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'app_test_forms/url_form.html', context)
        return HttpResponse(form.cleaned_data.items())









