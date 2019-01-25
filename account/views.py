from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate
from .forms import MyUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import MyUser
from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
import datetime


def creation(request):
    now_date1 = str(datetime.date.today().year - 18)[2:3]
    now_date2 = str(datetime.date.today().year - 18)[3:4]
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Подтверждение E-mail Вашей учетной записи rypy.ru entertainment'
            text_message = render_to_string('account/acc-active-email.txt', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            html_message = render_to_string('account/acc-active-email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            # email = EmailMessage(subject, message, to=[to_email])
            # email.send()
            email = EmailMultiAlternatives(subject, text_message, to=[to_email])
            email.attach_alternative(html_message, "text/html")
            email.send()
            return render(request, 'account/acc-confirm-email.html', {'email': to_email})
            # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            context = {
                'form': form,
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'birthday': request.POST['birthday'],
                'month_off': '',
                'month_of_birth': request.POST['month_of_birth'],
                'now_date1': now_date1,
                'now_date2': now_date2,
                'year_of_birth': request.POST['year_of_birth'],
                'username': request.POST['username'],
                'email': request.POST['email'],
            }
            return render(request, 'account/acc-creation.html', context)
    else:
        form = MyUserForm()
    context = {
        'form': form,
        'now_date1': now_date1,
        'now_date2': now_date2,
        'month_off': 'disabled'
    }
    return render(request, 'account/acc-creation.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def profile(request):
    return render(request, 'account/acc-profile.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def login_redirect(request, site_redirect='menu'):
    context = {}
    context.update(csrf(request))

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(site_redirect)
        else:
            context['login_error'] = 'Пожалуйста, введите корректные адрес электронной почты и пароль учётной записи.' \
                                     ' Оба поля могут быть чувствительны к регистру.'
            return render_to_response('account/acc-login.html', context)
    else:
        return render_to_response('account/acc-login.html', context)






# from django.contrib import auth
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect, render_to_response
# from django.views import View
# from django.template.context_processors import csrf
# # Create your views here.
#
#
# def home(request):
#     return render(request, 'account/home.html')
#
#
# def login_redirect(request, site_redirect='menu'):
#     context = {}
#     context.update(csrf(request))
#
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = auth.authenticate(email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect(site_redirect)
#         else:
#             context['login_error'] = 'Пожалуйста, введите корректные адрес электронной почты и пароль учётной записи.' \
#                                      ' Оба поля могут быть чувствительны к регистру.'
#             return render_to_response('account/acc-login.html', context)
#     else:
#         return render_to_response('account/acc-login.html', context)


# @login_required(login_url='/account/login')
# def profile(request):
#     return redirect('')
#
#


# from .forms import UserForm, UserExtendedForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
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
