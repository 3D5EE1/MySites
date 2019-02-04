from django.shortcuts import render

# Create your views here.


def about_me(request):
    return render(request, 'about_me/about-me.html')


def legal(request):
    return render(request, 'legal.html')


def license_agreement(request, site='rypy'):
    return render(request, 'about_me/license-agreement.html', {'site': site})


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def careers(request):
    return render(request, 'careers.html')


def about(request):
    return render(request, 'about.html')


def support(request):
    return render(request, 'support.html')


def contact(request):
    return render(request, 'contact.html')


def press(request):
    return render(request, 'press.html')


def api(request):
    return render(request, 'api.html')


def career_administrator(request):
    return render(request, 'career-administrator.html')