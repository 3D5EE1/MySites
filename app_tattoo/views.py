from django.shortcuts import render

# Create your views here.


def tattoo(request):
    return render(request, 'app_tattoo/tattoo.html')