from django.shortcuts import render

# Create your views here.


def planets(request):
    return render(request, 'planets/planets.html')