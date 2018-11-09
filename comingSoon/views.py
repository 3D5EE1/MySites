from django.shortcuts import render

# Create your views here.


def comingSoon(request):
    return render(request, 'comingSoon/comingSoon.html')