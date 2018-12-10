from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, UserExtendedForm
# Create your views here.


def login(request):
    return render(request, 'account/login.html', {})


class CreationView(View):
    context = {
        'user_form': UserForm,
        'user_extended_form': UserExtendedForm
    }

    def get(self, request):
        return render(request, "account/creation.html", self.context)

    def post(self, request):

        user_form = UserForm(request.POST)
        user_extended_form = UserExtendedForm(request.POST)

        if user_form.is_valid() and user_extended_form.is_valid():
            user_form.save()
            user_extended_form.save()
            return render(request, 'account/login.html', {})
        else:
            return render(request, "account/creation.html", self.context)
