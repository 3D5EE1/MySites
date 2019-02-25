from django.shortcuts import render
from message.forms import MessageForm

# Create your views here.


def about_me(request):
    return render(request, 'about_me/about-me.html')


def legal(request):
    return render(request, 'about_me/legal.html')


def license_agreement(request, site):
    return render(request, 'about_me/license-agreement.html', {'site': site})


def privacy_policy(request):
    return render(request, 'about_me/privacy-policy.html')


def careers(request):
    return render(request, 'about_me/careers.html')


def about(request):
    return render(request, 'about_me/about.html')


def support(request):
    return render(request, 'about_me/support.html')


def contact(request):
    message_form = MessageForm(request.POST)
    if request.method == 'POST' and message_form.is_valid():
        message_form.save()
        email = message_form.cleaned_data.get('email')
        return render(request, 'message/message-confirm.html', {'email': email})
    else:
        return render(request, 'about_me/contact.html')


def press(request):
    return render(request, 'about_me/press.html')


def api(request):
    return render(request, 'about_me/api.html')


def career_administrator(request):
    return render(request, 'about_me/career-administrator.html')


def coming_soon(request):
    return render(request, 'message/coming-soon.html')


