from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, UserExtendedForm
# Create your views here.


def home(request):
    return redirect(auth_app)


def auth_app(request):
    return render(request, 'account/home.html')
















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
#             # user_extended.user_id = user_form.pk
#             # user_extended.save()
#             user_form.save()
#             return redirect('home')
#         else:
#             return render(request, "account/creation.html", self.context)
