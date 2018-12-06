from django.shortcuts import render
from django.http import HttpResponse
from coming_soon import forms


# Create your views here.


def coming_soon(request):
    return render(request, 'coming_soon/coming-soon.html')


def message(request):
    message_form = forms.MessageForm(request.POST)
    if request.method == 'POST' and message_form.is_valid():
        message_form.save()
        return HttpResponse('Ваше сообщение отправлено. Спасибо!')
