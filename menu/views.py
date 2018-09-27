from django.shortcuts import render

# Create your views here.


def menu(request):
    return render(request, 'menu/menu.html')

def menu1(request):
    return render(request, 'menu/menu1.html')

def menu2(request):
    return render(request, 'menu/menu2.html')