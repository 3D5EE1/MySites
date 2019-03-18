from django.shortcuts import render

# Create your views here.


def art(request):
    return render(request, 'app_art3d/art3d.html')