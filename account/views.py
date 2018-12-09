from django.shortcuts import render
from .forms import UserForm, UserExtendedForm
# Create your views here.


def login(request):
    return render(request, 'account/login.html', {})


def creation(request):
    context = {
        'user_form': UserForm(),
        'user_extended_form': UserExtendedForm()
    }
    return render(request, "account/creation.html", context)
