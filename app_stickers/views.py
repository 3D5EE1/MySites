from django.shortcuts import render

# Create your views here.


def stickers(request):
    return render(request, 'app_stickers/stickers.html')