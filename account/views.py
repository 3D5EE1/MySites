from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, UserExtendedForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def home(request):
    return redirect(auth_app_home)


@login_required(login_url='/account/auth-app/login')
def auth_app_home(request):
    return render(request, 'account/home.html')


def auth_app_sign_up(request):
    context = {
        'user_form': UserForm(),
        'user_extended_form': UserExtendedForm()
    }
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_extended_form = UserExtendedForm(request.POST, request.FILES)

        if user_form.is_valid() and user_extended_form.is_valid():

            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user_extended = user_extended_form.save(commit=False)
            new_user_extended.user = new_user
            new_user_extended.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            ))

            return redirect(auth_app_home)

    return render(request, 'account/sign_up.html', context)




# def login(request):
#     return render(request, 'account/login.html', {})
#
#
# class CreationView(View):
#     context = {
#         'user_form': UserForm(),
#         'user_extended_form': UserExtendedForm()
#     }
#
#     def get(self, request):
#         return render(request, "account/creation.html", self.context)
#
#     def post(self, request):
#
#         user_form = UserForm(request.POST)
#         user_extended_form = UserExtendedForm(request.POST, request.FILES)
#
#         if user_form.is_valid() and user_extended_form.is_valid():
#
#             # user_extended = user_extended_form.save(commit=False)
#             # user_extended.user = user_form.user
#             # user_extended.save()
#             user_form.save()
#             return redirect('home')
#         else:
#             return render(request, "account/creation.html", self.context)
