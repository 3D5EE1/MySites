from django.shortcuts import render
from .forms import UserForm, AccountForm
# Create your views here.


def login(request):
    return render(request, 'account/login.html', {})


def creation(request):
    context = {
        'user_form': UserForm(),
        'account_form': AccountForm()
    }
    return render(request, "account/creation.html", context)


def profile(request):
    return render(request, "account/profile.html", {})


