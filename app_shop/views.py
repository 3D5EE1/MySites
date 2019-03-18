from django.shortcuts import render

# Create your views here.


def shop(request):
    return render(request, 'app_shop/shop.html')