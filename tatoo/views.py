from django.shortcuts import render

# Create your views here.


def tatoo (request):
    return render(request, 'tatoo/tatoo.html')