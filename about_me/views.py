from django.shortcuts import render

# Create your views here.


def about_me(request):
    return render(request, 'about_me/about-me.html')


def license_agreement(request, site='rypy'):
    return render(request, 'about_me/license-agreement.html', {'site': site})