from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views import View

# Create your views here.
from django.template.context_processors import csrf


@login_required(login_url='/account/login')
def profile(request):
    return redirect('')


def home(request):
    return render(request, 'account/home.html')


class Login(View):
    context = {}

    def get(self, request):
        return render(request, 'account/login.html', self.context)

    def post(self, reguest):
        self.context.update(csrf(reguest))
        if reguest.POST:
            email = reguest.POST.get('email')
            password = reguest.POST.get('password')
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(reguest, user)
                return redirect(home)
            else:
                self.context['login_error'] = 'Пользователь не найден'
                return render_to_response('account/login.html', self.context)
        else:
            return render_to_response('account/login.html', self.context)










# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import UserForm, UserExtendedForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# # Create your views here.
#
#
# def home(request):
#     return redirect(auth_app_home)
#
#
# @login_required(login_url='/test_account/auth-app/login')
# def auth_app_home(request):
#     return render(request, 'test_account/../../account/templates/account/home1.html')
#
#
# def auth_app_sign_up(request):
#     context = {
#         'user_form': UserForm(),
#         'user_extended_form': UserExtendedForm()
#     }
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         user_extended_form = UserExtendedForm(request.POST, request.FILES)
#
#         if user_form.is_valid() and user_extended_form.is_valid():
#
#             new_user = User.objects.create_user(**user_form.cleaned_data)
#             new_user_extended = user_extended_form.save(commit=False)
#             new_user_extended.user = new_user
#             new_user_extended.save()
#
#             login(request, authenticate(
#                 username=user_form.cleaned_data['username'],
#                 password=user_form.cleaned_data['password'],
#             ))
#
#             return redirect(auth_app_home)
#
#     return render(request, 'test_account/../../account/templates/account/sign_up.html', context)




# def login(request):
#     return render(request, 'test_account/login1.html', {})
#
#
# class CreationView(View):
#     context = {
#         'user_form': UserForm(),
#         'user_extended_form': UserExtendedForm()
#     }
#
#     def get(self, request):
#         return render(request, "test_account/creation1.html", self.context)
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
#             return render(request, "test_account/creation1.html", self.context)
