from django.shortcuts import render

# Create your views here.


def stickers(request):
    return render(request, 'stickers/stickers.html')